import React from 'react'
import { Form, Input, Button, message } from 'antd'
import { login } from '../api'

export default function Login({ onSuccess }){
  const [loading, setLoading] = React.useState(false)
  const onFinish = async (values) =>{
    setLoading(true)
    try{
      const data = await login(values.username, values.password)
      localStorage.setItem('token', data.access_token)
      message.success('登录成功')
      onSuccess && onSuccess()
    }catch(err){
      console.error(err)
      message.error(err?.response?.data?.detail || '登录失败')
    }finally{setLoading(false)}
  }
  return (
    <Form onFinish={onFinish} style={{ maxWidth: 420 }}>
      <Form.Item name="username" rules={[{ required: true }] }>
        <Input placeholder="用户名" />
      </Form.Item>
      <Form.Item name="password" rules={[{ required: true }] }>
        <Input.Password placeholder="密码" />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit" loading={loading}>登录</Button>
      </Form.Item>
    </Form>
  )
}
