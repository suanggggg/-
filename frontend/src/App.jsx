import React from 'react'
import { ConfigProvider } from 'antd'
import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import Assessment from './pages/Assessment'

export default function App(){
  const [route, setRoute] = React.useState('login')
  return (
    <ConfigProvider>
      <div style={{ padding: 24 }}>
        <div style={{ marginBottom: 12 }}>
          <button onClick={()=>setRoute('login')}>Login</button>{' '}
          <button onClick={()=>setRoute('register')}>Register</button>{' '}
          <button onClick={()=>setRoute('dashboard')}>Dashboard</button>{' '}
          <button onClick={()=>setRoute('assessment')}>Assessment</button>
        </div>
        {route === 'login' && <Login onSuccess={()=>setRoute('dashboard')} />}
        {route === 'register' && <Register onSuccess={()=>setRoute('login')} />}
        {route === 'dashboard' && <Dashboard />}
        {route === 'assessment' && <Assessment />}
      </div>
    </ConfigProvider>
  )
}
