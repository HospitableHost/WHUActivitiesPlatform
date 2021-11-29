<template>
  <div class="container" style="overflow:auto;">
    <el-descriptions title="活动信息" :border='false' :column='8'>
      <el-descriptions-item label="活动标题" :span='8' :labelStyle="{'text-align': 'center'}" :contentStyle="{'text-align': 'center'}">{{activityInfo.activity_title}}</el-descriptions-item>
      <el-descriptions-item label="发布组织" :span='4' :labelStyle="{'text-align': 'center'}" :contentStyle="{'text-align': 'center'}">{{activityInfo.organization_name}}</el-descriptions-item>
      <el-descriptions-item label="面向院系" :span='4' :labelStyle="{'text-align': 'center'}" :contentStyle="{'text-align': 'center'}">{{activityInfo.oriented_department}}</el-descriptions-item>
      <el-descriptions-item label="活动类型" :span='2' :labelStyle="{'text-align': 'center'}" :contentStyle="{'text-align': 'center'}">{{activityInfo.activity_type}}</el-descriptions-item>
      <el-descriptions-item label="状态" :span='2' :labelStyle="{'text-align': 'center'}" :contentStyle="{'text-align': 'center'}">
        <el-tag size="small" :type="activityInfo.activity_status | statusFilter">{{activityInfo.activity_status}}</el-tag>
      </el-descriptions-item>
      <el-descriptions-item label="发布时间" :span='2' :labelStyle="{'text-align': 'center'}" :contentStyle="{'text-align': 'center'}">{{activityInfo.publish_time}}</el-descriptions-item>
      <el-descriptions-item label="报名截止时间" :span='2' :labelStyle="{'text-align': 'center'}" :contentStyle="{'text-align': 'center'}">{{activityInfo.parti_ddl}}</el-descriptions-item>
      <el-descriptions-item label="活动详情" :span='8' :labelStyle="{'text-align': 'center'}">{{activityInfo.activity_detail}}</el-descriptions-item>
    </el-descriptions>
    <br/>
    <el-descriptions title="活动评论"></el-descriptions>
    <div v-if='comments.length==0'>暂无评论</div>
    <div style="overflow:auto; height:600px;" v-if='comments.length!==0'>   
    <div class="comment" v-for="(item,indexOfFather) in comments" :key='item.comment_id'>
      <div class="info">
        <img class="avatar" :src="item.user_avatar" width="36" height="36"/>
        <div class="right">
          <div class="name">{{item.user_nickname}}</div>
          <div class="date">{{item.comment_time}}</div>
        </div>
      </div>
      <div class="content">{{item.comment_content}}</div>
      <div class="control">
        <!-- <span class="like" :class="{active: item.isLike}" @click="likeClick(item)">
          <i class="iconfont icon-like"></i>
          <span class="like-num">{{item.likeNum > 0 ? item.likeNum + '人赞' : '赞'}}</span>
        </span> -->
        <span class="comment-reply" @click="showCommentInput(item, null,indexOfFather)">
          <i class="iconfont icon-comment"></i>
          <span>回复</span>
        </span>
        <span class="comment-reply" @click="deleteComment(item.comment_id, true, indexOfFather, -1)">
          <i class="iconfont icon-comment"></i>
          <span>删除</span>
        </span>
      </div>
      <div class="reply">
        <div class="item" v-for="(reply,indexOfChild) in item.reply" :key='reply.comment_id'>
          <div class="reply-content">
            <span class="from-name">{{reply.user_nickname}}</span><span>: </span>
            <span class="to-name">@{{reply.to_user_nickname}}</span>
            <span>{{reply.comment_content}}</span>
          </div>
          <div class="reply-bottom">
            <span>{{reply.comment_time}}</span>
            <span class="reply-text" @click="showCommentInput(item, reply, indexOfFather)">
              <i class="iconfont icon-comment"></i>
              <span>回复</span>
            </span>
            <span class="reply-text" @click="deleteComment(reply.from_comment_id, false, indexOfFather, indexOfChild)">
              <i class="iconfont icon-comment"></i>
              <span>删除</span>
            </span>
          </div>
        </div>
        <transition name="fade">
          <div class="input-wrapper" v-if="showItemId === item.comment_id">
            <el-input class="gray-bg-input"
                      v-model="inputComment"
                      type="textarea"
                      :rows="3"
                      autofocus
                      placeholder="写下你的回复">
            </el-input>
            <div class="btn-control">
              <span class="cancel" @click="cancel">取消</span>
              <el-button class="btn" type="success"  @click="postCommentToComment()">确定</el-button>
            </div>
          </div>
        </transition>
        </div>

      </div>
    </div>
    <br/>
    <el-descriptions title="发表评论"></el-descriptions>
    <div class="write-reply" >
      <div class="input-wrapper" v-if="true">
        <el-input class="gray-bg-input"
                  v-model="commentToActivity"
                  type="textarea"
                  :rows="4"
                  autofocus
                  placeholder="写下你的评论">
        </el-input>
        <br/><br/>
        <el-button type="primary" icon="el-icon-edit" @click="postCommentToActivity" style="float:right;">发表评论</el-button>
      </div>
    </div>
  </div>
</template>

<script>

  import Vue from 'vue'
  import { deleteComment, newCommentToActivity, newCommentToComment } from '@/api/comment'

  export default {
    props: {
      comments: {
        type: Array,
        required: true
      },
      activityInfo: {
        required: true
      }
    },
    filters: {
      statusFilter(status) {
        const statusMap = {
          '正在报名': 'success',
          '报名截止': 'danger'
        }
        return statusMap[status]
      }
    },
    data() {
      return {
        inputComment: '',
        showItemId: '',
        commentToActivity: '',
        to_comment_id:'',
        indexOfF:-1
      }
    },
    computed: {},
    methods: {
      cancel() {
        this.showItemId = ''
        this.to_comment_id=''
        this.indexOfF=-1
      },
      postCommentToComment(to_comment_id) {
        newCommentToComment({user_id:this.$store.getters.token,
                             activity_id:this.$route.params.activity_id,
                             comment_time:new Date().toISOString().split('.')[0],
                             user_status:'组织管理员',
                             comment_content:this.inputComment,
                             father_comment_id:this.showItemId,
                             to_comment_id:this.to_comment_id}).then(response=>{
                               var commentInfo = response.commentInfo
                               commentInfo.comment_time = new Date(commentInfo.comment_time).toISOString().split('.')[0]
                              //  console.log(this.indexOfF)
                               Vue.set(this.comments[this.indexOfF].reply,this.comments[this.indexOfF].reply.length,commentInfo)
                               this.inputComment=''
                               this.showItemId=''
                               this.to_comment_id=''
                               this.indexOfF=-1
                               this.$message({
                                 type:'success',
                                 message:'回复成功'
                               })
                             })
      },
      showCommentInput(item, reply, indexOfFather) {
        if (reply) {
          this.inputComment = "@" + reply.user_nickname + " "
          this.to_comment_id = reply.from_comment_id
        } else {
          this.inputComment = "@" + item.user_nickname + " "
          this.to_comment_id = item.comment_id
        }
        this.showItemId = item.comment_id
        this.indexOfF=indexOfFather
        
      },
      deleteComment(comment_id, isFatherComment, indexOfFather, indexOfChild){
        if(isFatherComment){
          deleteComment({admin_userid:this.$store.getters.token, comment_id:comment_id}).then(response=>{
            Vue.delete(this.comments,indexOfFather)
            this.$message({
              type:'success',
              message:'删除成功'
            })
          })          
        }else{
          deleteComment({admin_userid:this.$store.getters.token, comment_id:comment_id}).then(response=>{
            Vue.delete(this.comments[indexOfFather].reply,indexOfChild)
            this.$message({
              type:'success',
              message:'删除成功'
            })
          })          
        }
      },
      postCommentToActivity(){
        let comment_time = new Date().toISOString().split('.')[0]
        comment_time = comment_time.split('T')[0]+' '+comment_time.split('T')[1]
        newCommentToActivity({user_id:this.$store.getters.token,
                              activity_id:this.$route.params.activity_id,
                              comment_time:comment_time,
                              // comment_time:new Date().toISOString(),
                              comment_content:this.commentToActivity,
                              user_status:'组织管理员'}).then(response=>{
                                var newComment = response.commentInfo
                                // console.log(newComment.comment_time)
                                Vue.set(newComment,'reply',[])
                                newComment.comment_time=new Date(newComment.comment_time+'+00:00').toLocaleString()
                                Vue.set(this.comments,this.comments.length,newComment)                        
                                this.commentToActivity=''
                                this.$message({
                                  type:'success',
                                  message:'评论成功'
                                })                                
                              })
      }
    }
  }
</script>

<style scoped lang="scss">
  .container {
    padding: 0 10px;
    box-sizing: border-box;
    .comment {
      display: flex;
      flex-direction: column;
      padding: 10px;
      border-bottom: 1px solid #F2F6FC;
      .info {
        display: flex;
        align-items: center;
        .avatar {
          border-radius: 50%;
        }
        .right {
          display: flex;
          flex-direction: column;
          margin-left: 10px;
          .name {
            font-size: 16px;
            color: #303133;
            margin-bottom: 5px;
            font-weight: 500;
          }
          .date {
            font-size: 12px;
            color: #909399;
          }
        }
      }
      .content {
        font-size: 16px;
        color: #303133;
        line-height: 20px;
        padding: 10px 0;
      }
      .control {
        display: flex;
        align-items: center;
        font-size: 14px;
        color: #909399;
        .like {
          display: flex;
          align-items: center;
          margin-right: 20px;
          cursor: pointer;
          &.active, &:hover {
            color: #409EFF;
          }
          .iconfont {
            font-size: 14px;
            margin-right: 5px;
          }
        }
        .comment-reply {
          display: flex;
          align-items: center;
          cursor: pointer;
          &:hover {
            color: #333;
          }
          .iconfont {
            font-size: 16px;
            margin-right: 5px;
          }
        }

      }
      .reply {
        margin: 10px 0;
        border-left: 2px solid #DCDFE6;
        .item {
          margin: 0 10px;
          padding: 10px 0;
          border-bottom: 1px dashed #EBEEF5;
          .reply-content {
            display: flex;
            align-items: center;
            font-size: 14px;
            color: #303133;
            .from-name {
              color: #409EFF;
            }
            .to-name {
              color: #409EFF;
              margin-left: 5px;
              margin-right: 5px;
            }
          }
          .reply-bottom {
            display: flex;
            align-items: center;
            margin-top: 6px;
            font-size: 12px;
            color: #909399;
            .reply-text {
              display: flex;
              align-items: center;
              margin-left: 10px;
              cursor: pointer;
              &:hover {
                color: #333;
              }
              .icon-comment {
                margin-right: 5px;
              }
            }
          }
        }
        .write-reply {
          display: flex;
          align-items: center;
          font-size: 14px;
          color: #909399;
          padding: 10px;
          cursor: pointer;
          &:hover {
            color: #303133;
          }
          .el-icon-edit {
            margin-right: 5px;
          }
        }
        .fade-enter-active, fade-leave-active {
          transition: opacity 0.5s;
        }
        .fade-enter, .fade-leave-to {
          opacity: 0;
        }
        .input-wrapper {
          padding: 10px;
          .gray-bg-input, .el-input__inner {
            /*background-color: #67C23A;*/
          }
          .btn-control {
            display: flex;
            justify-content: flex-end;
            align-items: center;
            padding-top: 10px;
            .cancel {
              font-size: 16px;
              color: #606266;
              margin-right: 20px;
              cursor: pointer;
              &:hover {
                color: #333;
              }
            }
            .confirm {
              font-size: 16px;
            }
          }
        }
      }
    }
  }
</style>