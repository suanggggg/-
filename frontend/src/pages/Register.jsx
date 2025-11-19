import React from 'react'
import { Form, Input, Button, message } from 'antd'
import { register } from '../api'

export default function Register({ onSuccess }){
  const [loading, setLoading] = React.useState(false)
  const onFinish = async (values) =>{
    setLoading(true)
    try{
      await register(values.username, values.password)
      message.success('注册成功，请登录')
      onSuccess && onSuccess()
    }catch(err){
      console.error(err)
      message.error(err?.response?.data?.detail || '注册失败')
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
        <Button type="primary" htmlType="submit" loading={loading}>注册</Button>
      </Form.Item>
    </Form>
  )
}
