<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="加载中"
      border
      fit
      highlight-current-row
      height="630"
    >
      <el-table-column align="center" label="序号" width="75" :resizable="false">
        <template slot-scope="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="活动标题" width="400" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.activity_title }}
        </template>
      </el-table-column>
      <el-table-column label="发布组织" width="350" align="center" :resizable="false">
        <template slot-scope="scope">
          <span>{{ scope.row.organization_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="活动类型" width="150" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.activity_type }}
        </template>
      </el-table-column>
      <el-table-column label="面向院系" width="150" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.oriented_department }}
        </template>
      </el-table-column>
      <el-table-column label="活动详情" width="550" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.activity_detail }}
        </template>
      </el-table-column>
      <el-table-column label="活动海报" width="150" align="center" :resizable="false">
        <template slot-scope="scope">
          <el-link icon="el-icon-picture" :href="scope.row.activity_post" target='_blank'>点击查看</el-link>
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="状态" width="150" align="center" :resizable="false">
        <template slot-scope="scope">
          <el-tag :type="scope.row.activity_status | statusFilter">{{ scope.row.activity_status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="published_at" label="发布时间" width="200" :resizable="false">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.publish_time }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="end_at" label="报名截止时间" width="200" :resizable="false">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.parti_ddl }}</span>
        </template>
      </el-table-column>
      <el-table-column
        fixed="right"
        label="操作"
        width="180"
        align="center"
        :resizable="false">
        <template slot-scope="scope">
          <el-button
            @click.native.prevent="deleteActivity(scope.$index)"
            type="text"
            size="small"
            icon='el-icon-delete-solid'>
            删除活动
          </el-button>
          <el-button
            @click.native.prevent="getComments(scope.$index)"
            type="text"
            size="small"
            icon='el-icon-s-comment'>
            查看评论
          </el-button>
          <el-button
            @click.native.prevent="getParticipants(scope.$index)"
            type="text"
            icon='el-icon-s-check'
            size="small">
            查看报名情况
          </el-button>
        </template>
      </el-table-column>
      <div slot="empty" style="height:200px;line-height: 200px;text-align: left;font-size:30px;" :resizable="false">
      <i class="el-icon-warning-outline"></i>暂未发布过活动
      </div>      
    </el-table>
  </div>
</template>

<script>
import { getMyActivities, deleteActivity } from '@/api/table'
import Vue from 'vue'
export default {
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
      list: null,
      listLoading: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getMyActivities({admin_userid:this.$store.getters.token}).then(response => {
        this.list = response.data
        for(let i=0; i<this.list.length; i++){
          // console.log('服务器传回的第'+i+'个活动的报名截止时间是：'+this.list[i].parti_ddl)
          const ddlDate = new Date(this.list[i].parti_ddl+'+00:00')
          if(ddlDate>new Date()){
            this.list[i]['activity_status']='正在报名'
          }
          else{
            this.list[i]['activity_status']='报名截止'
          }
          // console.log('服务器传回的第'+i+'个活动的发布时间是：'+this.list[i].publish_time)
          const publishDate = new Date(this.list[i].publish_time+'+00:00')
          this.list[i].parti_ddl=ddlDate.toLocaleString()
          this.list[i].publish_time=publishDate.toLocaleString()
          // console.log('处理后的第'+i+'个活动的报名截止时间是：'+this.list[i].parti_ddl)
          // console.log('处理后的第'+i+'个活动的报名发布时间是：'+this.list[i].publish_time)
        }
        this.listLoading = false
      })
    },
    deleteActivity(index)
    {
      deleteActivity({activity_id:this.list[index].activity_id,admin_userid:this.$store.getters.token}).then(response=>{
        Vue.delete(this.list,index)
        this.$message({
          message:"删除成功",
          type:'success'
        })
      })
    },
    getParticipants(index)
    {
      this.$router.push({ path: 'myActivities/participants/activity_id='+this.list[index].activity_id})
    },
    getComments(index){
      this.$router.push({ path: 'myActivities/comments/activity_id='+this.list[index].activity_id})
    }
  }
}
</script>
