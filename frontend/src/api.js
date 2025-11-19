import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: { 'Content-Type': 'application/json' }
})

// Attach token from localStorage to all requests
api.interceptors.request.use(cfg => {
  try{
    const t = localStorage.getItem('token')
    if(t) cfg.headers = cfg.headers || {}, cfg.headers.Authorization = `Bearer ${t}`
  }catch(e){
    // ignore in non-browser/SSR environments
  }
  return cfg
})

export async function register(username, password){
  const res = await api.post('/auth/register', { username, password })
  return res.data
}

export async function login(username, password){
  const res = await api.post('/auth/login', { username, password })
  return res.data
}

export async function me(token){
  const res = await api.get('/auth/me', { headers: { Authorization: `Bearer ${token}` }})
  return res.data
}

export default api

export async function createAssessment(user_id, type = 'mock_interview', media_ref = null){
  const res = await api.post('/assessments/', { user_id, type, media_ref })
  return res.data
}

export async function submitAssessmentScore(assessment_id, system_score){
  const res = await api.post(`/assessments/${assessment_id}/score`, { system_score })
  return res.data
}

export async function getAssessmentResults(assessment_id){
  const res = await api.get(`/assessments/${assessment_id}/results`)
  return res.data
}
