var app = getApp()

// pages/activity/activity.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    user_id:-1,
    activity_id:-1,
    organization_name:"",
    activity_type:"",
    activity_title:"",
    publish_time:"",
    activity_detail:"",
    activity_post:"",
    parti_ddl:"",
    oriented_department:"",
    comments:[],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options)
    var that = this
    that.setData({
      user_id:options.userid,
      activity_id:options.activityid,
      organization_name:options.organizationname,
      activity_type:options.activitytype,
      activity_title:options.activitytitle,
      publish_time:options.publishtime,
      activity_detail:options.activitydetail,
      activity_post:options.activitypost,
      parti_ddl:options.partiddl,
      oriented_department:options.orienteddepartment,
      status:options.status
    }),
    wx.request({
      url: app.globalData.base_path+'/comments_act_all/',
      method:"GET",
      header:{"content-type": "application/json"},
      data:{
        activity_id: that.data.activity_id
      },
      success: function(res){
        console.log(res.data)
        var data = res.data.data
        var com = []
        if(data.length > 0){
          
          for (var i = 0; i < data.length; i++){
            com.push(data[i])
          }
        }
        that.setData({
          comments: com
        })
      },
      fail: function(res){
        console.error("获取评论错误")
      }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  deleteComment() {
    wx.showModal({
      title: '提示',
      content: '确定要删除该评论吗？',
      success (res) {
        if (res.confirm) {
          console.log('用户点击确定')
          wx.request({  //删除评论

          })
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
  },

  switchShow(){
    let that = this;
    this.setData({isShow:!that.data.isShow});
  },

  new_com: function(res){
    this.setData({
      new_com_value: res.detail.value
    })
  },

  submit: function(e){
    wx.request({
      url: app.globalData.base_path+'comment_add/',
      method:"POST",
      header:{"content-type":"json"}
      
    })
  }
})