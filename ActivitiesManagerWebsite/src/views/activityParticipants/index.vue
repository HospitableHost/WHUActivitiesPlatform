<template>
  <div class="app-container">
    <template>
      <el-backtop :bottom='40' :right='5'>
        <div
          style="{
          height: 100%;
          width: 100%;
          background-color: #f2f5f6;
          box-shadow: 0 0 6px rgba(0,0,0, .12);
          text-align: center;
          line-height: 40px;
          color: #1989fa;
          }">
        UP
        </div>
      </el-backtop>
    </template>
    <el-table
      v-loading="listLoading"
      :data="participants"
      element-loading-text="加载中"
      border
      fit
      highlight-current-row
      class="participantsTable"
    >
      <el-table-column align="center" label="序号" width="50" :resizable="false">
        <template slot-scope="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="用户昵称" width="190" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.user_nickname }}
        </template>
      </el-table-column>
      <el-table-column label="用户姓名" width="180" align="center" :resizable="false">
        <template slot-scope="scope">
          <span>{{ scope.row.user_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="学号/工号" width="150" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.school_id }}
        </template>
      </el-table-column>
      <el-table-column label="所属学院/部门" width="220" align="center" :resizable="false">
        <template slot-scope="scope">
          {{ scope.row.department }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="是否被拉黑" width="100" align="center" :resizable="false">
        <template slot-scope="scope">
          <el-tag :type="scope.row.is_banned | banstatusFilter">{{ scope.row.is_banned }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="signup_at" label="报名时间" width="200" :resizable="false">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.parti_time }}</span>
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="审核状态" width="140" align="center" :resizable="false">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column
        label="拉黑"
        width="90"
        align="center"
        :resizable="false">
        <template slot-scope="scope">
          <el-button
            @click.native.prevent="ban(scope.$index)"
            type="danger"
            icon='el-icon-warning-outline'
            :resizable="false"
            :disabled="scope.row.is_banned==='是'"
            circle>
          </el-button>
        </template> 
      </el-table-column>
      <el-table-column
        label="报名审核"
        width="105"
        align="center"
        :resizable="false">
        <template slot-scope="scope">
          <el-button
            @click.native.prevent="signUpPass(scope.$index)"
            type="text"
            size="small"
            style="font-size:20px"
            :disabled="scope.row.pass_hidden"
            :resizable="false">
            ✔
          </el-button>
          <el-button
            @click.native.prevent="signUpRefuse(scope.$index)"
            type="text"
            size="small"
            style="font-size:20px"
            :disabled="scope.row.refuse_hidden"
            :resizable="false">
            ✘
          </el-button>
        </template> 
      </el-table-column>
      <div slot="empty" style="height:200px;line-height: 200px;text-align: left;font-size:30px;">
      <i class="el-icon-warning-outline"></i>暂无人报名
      </div>
    </el-table>

  </div>
</template>

<script>
import { getParticipants, dealSignUp } from '@/api/activityParticipants'
import { newBan } from '@/api/blacklist'
export default {
  filters: {
    banstatusFilter(status) {
      const statusMap = {
        '否': 'success',
        '是': 'danger'
      }
      return statusMap[status]
    },
    statusFilter(status) {
      const statusMap = {
        '报名审核通过': 'success',
        '报名审核不通过': 'danger',
        '报名暂未审核': 'warning'
      }
      return statusMap[status]
    }    
  },
  data() {
    return {
      participants: null,
      listLoading: true,
      descriptionForBan:''
    }
  },
  created() {
    this.fetchData(this.$route.params.activity_id)
  },
  methods: {
    fetchData(activity_id) {
      this.listLoading = true
      getParticipants({admin_userid:this.$store.getters.token,activity_id:activity_id}).then(response => {
        this.participants = response.data
        for(let i=0; i<this.participants.length; i++){
          const partiDate = new Date(this.participants[i].parti_time+'+00:00')
          this.participants[i].parti_time=partiDate.toLocaleString()
          if(this.participants[i].is_banned=='0'){
            this.participants[i].is_banned='否'
          }
          else{
            this.participants[i].is_banned='是'
          }
          if(this.participants[i].status=='0'){
            this.participants[i].status='报名暂未审核'
            this.participants[i]['pass_hidden']=false
            this.participants[i]['refuse_hidden']=false
          }
          else if(this.participants[i].status=='1'){
            this.participants[i].status='报名审核通过'
            this.participants[i]['pass_hidden']=true
            this.participants[i]['refuse_hidden']=true
          }
          else{
            this.participants[i].status='报名审核不通过'
            this.participants[i]['pass_hidden']=true
            this.participants[i]['refuse_hidden']=true
          }          
        }
        this.listLoading = false
      }).catch(error=>{
        this.participants = []
        this.listLoading = false
      })
    },
    signUpPass(index){
      dealSignUp({
        admin_userid:this.$store.getters.token,
        activity_id:this.$route.params.activity_id,
        user_id:this.participants[index].user_id,
        status:1}).then(response=>{
          this.participants[index].pass_hidden=true
          this.participants[index].refuse_hidden=true
          this.participants[index].status="报名审核通过"
          this.$message({
            message:"已通过其报名",
            type:"success"
          })
        })
    },
    signUpRefuse(index){
      dealSignUp({
        admin_userid:this.$store.getters.token,
        activity_id:this.$route.params.activity_id,
        user_id:this.participants[index].user_id,
        status:2}).then(response=>{
          this.participants[index].pass_hidden=true
          this.participants[index].refuse_hidden=true
          this.participants[index].status="报名审核不通过"
          this.$message({
            message:"已拒绝其报名",
            type:"success"
          })
          })
    },
    ban(index){
    const h = this.$createElement;
    var _this = this
    this.$msgbox({
        title: '请描述其恶劣行为：',
        message: h('div', {
            attrs: {
                class: 'el-textarea',
            },
        }, [
            h('textarea', {
                attrs: {                   
                    class: 'el-textarea__inner',
                    autocomplete: 'off',
                    rows: 5,
                    id:'descriptionForBan'
                },
                value: _this.descriptionForBan,
                on: { input: _this.onDescriptionInputChange }
            })
        ]),
        showCancelButton: true,
        confirmButtonText: '确认拉黑',
        cancelButtonText: '取消拉黑',
        beforeClose: (action, instance, done) => {
            if (action === 'confirm') {
                instance.confirmButtonLoading = true;
                instance.confirmButtonText = '拉黑中...';
                newBan({ org_admin_id: _this.$store.getters.token,
                         user_id: _this.participants[index].user_id,
                         activity_id: _this.$route.params.activity_id,
                         description: _this.descriptionForBan,
                         banned_time: new Date().toISOString().split('.')[0]}).then(response=>{
                           _this.participants[index].is_banned='是'
                           _this.$message({
                             type:'success',
                             message:'拉黑成功' 
                        })
                        instance.confirmButtonLoading = false;
                        instance.confirmButtonText = '确认拉黑';
                        document.getElementById("descriptionForBan").value=''
                        done()
                 }).catch(error=>{
                        instance.confirmButtonLoading = false;
                        instance.confirmButtonText = '确认拉黑';
                        document.getElementById("descriptionForBan").value=''
                        done()
                 })
            } else {
              this.$message({
                type:'info',
                message:'取消拉黑'
              })
              document.getElementById("descriptionForBan").value=''
              done()
            }

        }
    })      
    },
    onDescriptionInputChange() {
      this.descriptionForBan = document.getElementById("descriptionForBan").value;
    }
  }
}
</script>
