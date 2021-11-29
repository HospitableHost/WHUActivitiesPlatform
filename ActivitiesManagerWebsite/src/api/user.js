import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/adminuser/login/',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/adminuser/info',
    method: 'get',
    params: { token }
  })
}

export function logout(data) {
  return request({
    url: '/adminuser/logout',
    method: 'post',
    data
  })
}
