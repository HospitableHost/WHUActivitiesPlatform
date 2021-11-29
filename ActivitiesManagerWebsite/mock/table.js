const Mock = require('mockjs')

const data = Mock.mock({
  'items|10': [{
    activity_title: '计算机学院第十三届寝室文化节',
    organization_name: '计算机学院团委',
    activity_type: '文体竞赛',
    publish_time: "2021-11-21T13:10:00+08:00",
    parti_ddl: "2021-11-27T14:12:00+08:00",
    activity_id: '@integer(300, 5000)',
    oriented_department: '计算机学院',
    activity_detail: '@sentence(20, 30)',
    activity_post: 'http://dzq',
    user_id: 1
  }]
})

module.exports = [
  {
    url: '/activity_op',
    type: 'get',
    response: config => {
      const items = data.items
        return {
          code: 1000,
          data: items
      }

    }
  },
  {
    url: '/activity_op',
    type: 'delete',
    response: _ => {
      return {
        code: 1000,
        message: '删除失败'
      }
    }
  },
  {
    url: '/oneActivity',
    type: 'get',
    response: _ => {
      return {
        code: 1000,
        data: data.items[0]
      }
    }
  }  
]
