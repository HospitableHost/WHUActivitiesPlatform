const Mock = require('mockjs')

const data = Mock.mock({
  'blacklist|20': [{
    department: "测绘学院",
    banned_time: "2021-11-13T20:33:00+08:00",
    school_id: '2018302132252',
    user_name: '迪迦',
    user_nickname: '盖亚',
    banned_user_id: 1,
    description: '@sentence(20, 30)',
    activity_title: '计算机学院第三十四届零杯大赛',
    organization_name: '王涛',
    activity_type: '学科竞赛'
  }]
})

module.exports = [
  {
    url: '/blacklist',
    type: 'get',
    response: config => {
      const blacklist = data.blacklist
      return {
        code: 1000,
        data: blacklist
      }
    }
  },
  {
    url: '/blacklist',
    type: 'delete',
    response: config => {
      return {
        code: 1000,
        message: "解除成功"
      }
    }
  },
  {
    url: '/blacklist',
    type: 'post',
    response: config => {
      return {
        code: 1000,
        message: "拉黑成功"
      }
    }
  }

]
