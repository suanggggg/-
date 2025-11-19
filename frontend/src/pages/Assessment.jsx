import React from 'react'
import { Button, Input, message, Card } from 'antd'
import { me, createAssessment, submitAssessmentScore, getAssessmentResults } from '../api'
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer } from 'recharts'

const { TextArea } = Input

export default function Assessment(){
  const [assessmentId, setAssessmentId] = React.useState('')
  const [result, setResult] = React.useState(null)
  const [scoreJson, setScoreJson] = React.useState('')

  const create = async () => {
    const token = localStorage.getItem('token')
    if(!token){ message.warn('请先登录'); return }
    try{
      const user = await me(token)
      const a = await createAssessment(user.id)
      setAssessmentId(a.id)
      message.success('测评已创建: ' + a.id)
      await loadResults(a.id)
    }catch(err){
      console.error(err)
      message.error('创建测评失败')
    }
  }

  const loadResults = async (id = assessmentId) => {
    if(!id){ message.warn('请输入或创建测评 ID'); return }
    try{
      const r = await getAssessmentResults(id)
      setResult(r)
    }catch(err){
      console.error(err)
      message.error('获取结果失败')
    }
  }

  const submitScore = async () => {
    if(!assessmentId){ message.warn('请先创建或填写测评 ID'); return }
    let parsed
    try{ parsed = JSON.parse(scoreJson) } catch(e){ message.error('评分内容不是有效的 JSON'); return }
    try{
      const r = await submitAssessmentScore(assessmentId, parsed)
      setResult(r)
      message.success('评分已提交')
    }catch(err){
      console.error(err)
      message.error('提交评分失败')
    }
  }

  return (
    <Card title="测评（Assessment）">
      <div style={{ marginBottom: 12 }}>
        <Button type="primary" onClick={create}>创建新测评</Button>{' '}
        <Button onClick={()=>loadResults()}>加载结果</Button>
      </div>

      <div style={{ marginBottom: 12 }}>
        <Input placeholder="测评 ID" value={assessmentId} onChange={e=>setAssessmentId(e.target.value)} />
      </div>

      <div style={{ marginBottom: 12 }}>
        <TextArea rows={8} placeholder='输入 system_score JSON，例如 {"technical":80, "communication":70}' value={scoreJson} onChange={e=>setScoreJson(e.target.value)} />
      </div>

      <div style={{ marginBottom: 12 }}>
        <Button type="primary" onClick={submitScore}>提交评分</Button>
      </div>

      <div>
        <h4>结果（result）</h4>
        <pre style={{ background:'#f7f7f7', padding:12 }}>{result ? JSON.stringify(result, null, 2) : '尚无结果'}</pre>
        {/* 雷达图可视化 system_score */}
        {result && result.system_score && typeof result.system_score === 'object' && Object.keys(result.system_score).length > 0 && (
          <div style={{ width: 400, height: 320, margin: '24px auto' }}>
            <ResponsiveContainer width="100%" height="100%">
              <RadarChart cx="50%" cy="50%" outerRadius="80%" data={Object.entries(result.system_score).map(([key, value]) => ({ metric: key, score: value }))}>
                <PolarGrid />
                <PolarAngleAxis dataKey="metric" />
                <PolarRadiusAxis angle={30} domain={[0, 100]} />
                <Radar name="评分" dataKey="score" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
              </RadarChart>
            </ResponsiveContainer>
          </div>
        )}
      </div>
    </Card>
  )
}
