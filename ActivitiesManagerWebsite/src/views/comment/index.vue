<template>
<div class="app-container">
  <comment :comments="commentData" :activityInfo='activityInfo'></comment>
</div>
</template>

<script>
  import * as CommentData from '/mock/comment'
  import comment from '@/components/Comment/index'
  import { getOneActivity } from '@/api/table'
  import { getComments } from '@/api/comment'

  export default {
    components: {
      comment
    },
    data() {
      return {
        commentData: [],
        activityInfo:null
      }
    },
    created() {
        getComments({activity_id:this.$route.params.activity_id}).then(respones=>{
            this.commentData=respones.data
            for(let i=0;i<this.commentData.length;i++){
              this.commentData[i].comment_time=new Date(this.commentData[i].comment_time+'+00:00').toLocaleString()
              for(let j=0;j<this.commentData[i].reply.length;j++){
                this.commentData[i].reply[j].comment_time=new Date(this.commentData[i].reply[j].comment_time+'+00:00').toLocaleString()
              }
            }
        })
        getOneActivity({admin_userid:this.$store.getters.token,activity_id:this.$route.params.activity_id}).then(response=>{
            this.activityInfo=response.data
            const ddlDate = new Date(this.activityInfo.parti_ddl+'+00:00')
            if(ddlDate>new Date()){
                this.activityInfo['activity_status']='正在报名'
            }
            else{
                this.activityInfo['activity_status']='报名截止'
            }
            const publishDate = new Date(this.activityInfo.publish_time+'+00:00')
            this.activityInfo.parti_ddl=ddlDate.toLocaleString()
            this.activityInfo.publish_time=publishDate.toLocaleString()
        })


    }
  }
</script>