import request from '@/utils/request'

export function getComments(params) {
  return request({
    url: '/comments_act_all/',
    method: 'get',
    params
  })
}

export function deleteComment(params) {
  return request({
    url: '/comment_delete/',
    method: 'delete',
    params
  })
}

export function newCommentToActivity(data) {
  return request({
    url: '/comment_addToActivity/',
    method: 'post',
    data
  })
}

export function newCommentToComment(data) {
    return request({
      url: '/comment_add/',
      method: 'post',
      data
    })
  }