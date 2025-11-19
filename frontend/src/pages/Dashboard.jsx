import React from 'react'
import { Button, Descriptions, message } from 'antd'
import { me } from '../api'

export default function Dashboard(){
  const [user, setUser] = React.useState(null)
  const load = async ()=>{
    const token = localStorage.getItem('token')
    if(!token){ message.warn('请先登录'); return }
    try{
      const u = await me(token)
      setUser(u)
    }catch(err){
      console.error(err)
      message.error('获取用户信息失败')
    }
  }
  React.useEffect(()=>{ load() }, [])
  return (
    <div>
      <h2>Dashboard</h2>
      {user ? (
        <Descriptions column={1} bordered>
          <Descriptions.Item label="用户名">{user.username}</Descriptions.Item>
          <Descriptions.Item label="贡献分">{user.points_balance}</Descriptions.Item>
        </Descriptions>
      ) : <div>未加载用户信息</div>}
      <div style={{ marginTop: 12 }}>
        <Button onClick={load}>刷新</Button>
      </div>
    </div>
  )
}
