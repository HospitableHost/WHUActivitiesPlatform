const Mock = require('mockjs')

const data = Mock.mock({
  'participants|20': [{
    department: "计算机学院",
    parti_time: "2021-11-27T14:12:00+08:00",
    is_banned: '0',
    school_id: '2018302110264',
    user_name: '党自强',
    user_nickname: 'JackDang',
    user_id: 1,
    status: '0'
  }]
})

module.exports = [
  {
    url: '/participants',
    type: 'get',
    response: config => {
      const participants = data.participants
      return {
        code: 1000,
        data: participants
      }
    }
  },
  {
    url: '/signup',
    type: 'put',
    response: config => {
      return {
        code: 1000,
        message: "修改成功"
      }
    }
  }    
]