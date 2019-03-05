<template>
  <div class="app-container">
    <el-button @click="getHost">test</el-button>
    <el-cascader
      :options="hostgroup"
      placeholder="所有"
      filterable
      expand-trigger="hover"
      change-on-select
      size="mini"/>
    <el-button-group>
      <el-button type="primary" size="mini">创建设备</el-button>
      <el-button type="primary" size="mini">导入</el-button>
    </el-button-group>

    <el-button round size="mini" style="float: right" @click="show=!show">过滤器</el-button>

    <transition name="el-fade-in-linear">
      <el-row :gutter="20" type="flex" justify="center">
        <el-form
          v-show="show"
          ref="form"
          :model="form"
          size="mini"
          label-position="right"
          label-width="55px">

          <el-form-item>
            <el-col :span="12">
              <el-form-item label="名称">
                <el-input v-model="input"/>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="IP地址">
                <el-input v-model="input"/>
              </el-form-item>
            </el-col>
          </el-form-item>

          <el-form-item>
            <el-col :span="12">
              <el-form-item label="品牌">
                <el-input v-model="input"/>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="型号">
                <el-input v-model="input"/>
              </el-form-item>
            </el-col>
          </el-form-item>

          <el-form-item>
            <el-col :span="12">
              <el-form-item label="类型">
                <el-select v-model="value" placeholder="">
                  <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"/>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="系统">
                <el-select v-model="value" placeholder="">
                  <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"/>
                </el-select>
              </el-form-item>
            </el-col>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" size="mini" @click="submitForm('ruleForm2')">查询</el-button>
            <el-button size="mini" @click="resetForm('ruleForm2')">重置</el-button>
          </el-form-item>

        </el-form>
      </el-row>
    </transition>

    <el-card class="box-card" style="margin-top: 20px">
      <el-row type="flex" justify="center">
        <el-table
          :data="host.slice((currentPage-1)*pageSize,currentPage*pageSize)"
          :default-sort = "{prop: 'name'}"
          style="width: 100%"
          tooltip-effect="dark"
          size="small">

          <el-table-column
            type="selection"
            align="center"/>
          <el-table-column
            label="状态"
            align="center"
            width="60px">
            <template slot-scope="host">
              <svg-icon v-if="host.row.snmp_available==='1'" icon-class="round_check_fill"/>
              <svg-icon v-else-if="host.row.snmp_available==='2'" icon-class="round_close_fill"/>
              <svg-icon v-else icon-class="round_question_fill"/>
            </template>
          </el-table-column>
          <el-table-column
            prop="name"
            label="名称"
            sortable
            width="180px"/>
          <el-table-column
            prop="interfaces[0].ip"
            label="接口"
            sortable
            width="180px"/>
          <el-table-column
            prop="inventory.vendor"
            label="品牌"
            sortable/>
          <el-table-column
            prop="inventory.model"
            label="型号"
            sortable
            width="120px"/>
          <el-table-column
            prop="inventory.type"
            label="类型"
            sortable/>
          <el-table-column
            prop="inventory.tag"
            label="系统"
            sortable/>
          <el-table-column
            prop="status"
            label="启用/禁用"
            sortable
            align="center">
            <template slot-scope="host">
              <el-switch
                v-model="host.row.status"
                active-color="#67C23A"
                inactive-color="#F56C6C"
                @change="handleSwitch(scope.row,scope.$index)"/>
            </template>
          </el-table-column>
        </el-table>
      </el-row>
      <el-pagination
        :total="host.length"
        :current-page="currentPage"
        :page-sizes="[10,20,50]"
        :page-size="20"
        layout="sizes,prev, pager, next"
        @current-change="handleCurrentChange"
        @size-change="handleSizeChange"/>

      <el-button type="text">启用</el-button>
      <el-button type="text">禁用</el-button>
      <el-button type="text">批量更新</el-button>
      <el-button type="text">删除</el-button>
    </el-card>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      show: true,
      host: [],
      hostgroup: [],
      currentPage: 1,
      pageSize: 20
    }
  },
  mounted() {
    this.getHostgroup()
  },
  methods: {
    getHostgroup() {
      var that = this
      const path = 'http://127.0.0.1:5000/asset/network'
      axios.get(path).then(function(response) {
        var data = response.data.hostgroup
        that.hostgroup = data
      })
    },
    getHost() {
      var that = this
      const path = 'http://127.0.0.1:5000/asset/network'
      axios.post(path).then(function(response) {
        var data = response.data.host
        that.host = data
      })
    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage
    },
    handleSizeChange(pageSize) {
      this.pageSize = pageSize
    }
  }
}
</script>
