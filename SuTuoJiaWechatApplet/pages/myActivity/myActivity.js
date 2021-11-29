const app = getApp()

// pages/comment/comment.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    currentTab:0,
    type:app.globalData.type,
    college:app.globalData.college,
    status:app.globalData.status,
    activities:[],
    on_act:[],
    over_act:[],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: app.globalData.base_path+'/enrollment_all',
      method:'GET',
      data:{user_id: app.globalData.user_id},
      header:{"Content-Type":"application/json"},
      success: function(res){
        console.log(res.data);
        var data = res.data.activities;
        if (data.length > 0) {
          var allactivities = [];
          var on_activities = [];
          var over_activities = [];
          var Utils = require ( '../../utils/util.js' );

          for (var i = 0; i < data.length; i++) {
            allactivities.push(data[i]);
            if(allactivities[i].parti_ddl >=  Utils.formatTime(new Date())){
              allactivities[i].status = "正在报名"
              on_activities.push(allactivities[i])
            }
            else{
              allactivities[i].status = "报名截止"
              over_activities.push(allactivities[i])
            }
          }
          console.log(on_activities)
          that.setData({ activities: allactivities });
          that.setData({ on_act: on_activities });
          that.setData({ over_act: over_activities });
        }
      },
      fail: function(){
        console.error("获取活动失败")
      },
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

  tapTab: function (e) {
    console.log(e.currentTarget.dataset.ctab);
    let index = e.currentTarget.dataset.ctab
    this.setData({currentTab:index});
  },

  toInfo: function(e){
    let userid = e.currentTarget.dataset.userid
    let activityid = e.currentTarget.dataset.activityid
    let activitytitle = e.currentTarget.dataset.activitytitle
    let activitytype = e.currentTarget.dataset.activitytype
    let activitydetail = e.currentTarget.dataset.activitydetail
    let organizationname = e.currentTarget.dataset.organizationname
    let partiddl = e.currentTarget.dataset.partiddl
    let publishtime = e.currentTarget.dataset.publishtime
    let orienteddepartment = e.currentTarget.dataset.orienteddepartment
    let activitypost = e.currentTarget.dataset.activitypost
    let status = e.currentTarget.dataset.status
    wx.navigateTo({
      url: '../activity/activity?userid='+userid+'&activityid='+activityid+'&activitytitle='+activitytitle+'&activitytype='+activitytype+'&activitydetail='+activitydetail+'&organizationname='+organizationname+
      '&partiddl='+partiddl+'&publishtime='+publishtime+'&orienteddepartment='+orienteddepartment+'&status='+status+'&activitypost='+activitypost
    })
  }
})