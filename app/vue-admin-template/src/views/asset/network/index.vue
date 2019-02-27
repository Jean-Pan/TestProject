<template>
  <div class="app-container">
    <el-button @click="getDate">{{ testing }}</el-button>

    <el-cascader
      :options="hostgroup"
      placeholder="所有"
      filterable
      expand-trigger="hover"
      change-on-select
      size="mini"
      @click="getDate"/>
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
          :data="network"
          :default-sort = "{prop: 'name'}"
          style="width: 100%"
          tooltip-effect="dark"
          size="medium">

          <el-table-column
            type="selection"
            align="center"/>
          <el-table-column
            label="状态"
            align="center"
            width="60px">
            <template slot-scope="tableData">
              <svg-icon v-if="tableData.row.available==='1'" icon-class="round_check_fill"/>
              <svg-icon v-else-if="tableData.row.available==='2'" icon-class="round_close_fill"/>
              <svg-icon v-else icon-class="round_question_fill"/>
            </template>
          </el-table-column>
          <el-table-column
            prop="name"
            label="名称"
            sortable
            width="120px"/>
          <el-table-column
            prop="interface"
            label="接口"
            sortable
            width="120px"/>
          <el-table-column
            prop="vendor"
            label="品牌"
            sortable/>
          <el-table-column
            prop="model"
            label="型号"
            sortable
            width="120px"/>
          <el-table-column
            prop="type"
            label="类型"
            sortable/>
          <el-table-column
            prop="tag"
            label="系统"
            sortable/>
          <el-table-column
            prop="status"
            label="启用/禁用"
            sortable
            align="center">
            <template slot-scope="tableData">
              <el-switch
                v-model="tableData.row.status"
                active-color="#67C23A"
                inactive-color="#F56C6C"
                @change="handleSwitch(scope.row,scope.$index)"/>
            </template>
          </el-table-column>
        </el-table>
      </el-row>

      <el-pagination
        :total="50"
        layout="prev, pager, next"/>
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
      testing: 'resp',
      show: true,
      network: [
        {
          available: '0',
          name: 'Aest Machine',
          vendor: 'H3C',
          model: 'H3C 3600',
          interface: '127.0.0.1',
          type: '交换机',
          tag: '旅服系统',
          status: true
        }, {
          available: '1',
          name: 'Cest Machine',
          vendor: 'H3C',
          model: 'H3C 3600',
          interface: '127.0.0.5',
          type: '交换机',
          tag: '旅服系统',
          status: false
        }, {
          available: '0',
          name: 'Dest Machine',
          vendor: 'H3C',
          model: 'H3C 3600',
          interface: '127.0.0.3',
          type: '交换机',
          tag: '旅服系统',
          status: true
        }, {
          available: '2',
          name: 'Gest Machine',
          vendor: 'H3C',
          model: 'H3C 3600',
          interface: '127.0.0.2',
          type: '交换机',
          tag: '旅服系统',
          status: false
        }, {
          available: '0',
          name: 'Test Machine',
          vendor: 'H3C',
          model: 'H3C 3600',
          interface: '127.0.0.1',
          type: '交换机',
          tag: '旅服系统',
          status: false
        }
      ],
      hostgroup: [
        {
          value: 'zhinan',
          label: '指南',
          children: [{
            value: 'shejiyuanze',
            label: '设计原则',
            children: [{
              value: 'yizhi',
              label: '一致'
            }, {
              value: 'fankui',
              label: '反馈'
            }, {
              value: 'xiaolv',
              label: '效率'
            }, {
              value: 'kekong',
              label: '可控'
            }]
          }, {
            value: 'daohang',
            label: '导航',
            children: [{
              value: 'cexiangdaohang',
              label: '侧向导航'
            }, {
              value: 'dingbudaohang',
              label: '顶部导航'
            }]
          }]
        }, {
          value: 'zujian',
          label: '组件',
          children: [{
            value: 'basic',
            label: 'Basic',
            children: [{
              value: 'layout',
              label: 'Layout 布局'
            }, {
              value: 'color',
              label: 'Color 色彩'
            }, {
              value: 'typography',
              label: 'Typography 字体'
            }, {
              value: 'icon',
              label: 'Icon 图标'
            }, {
              value: 'button',
              label: 'Button 按钮'
            }]
          }, {
            value: 'form',
            label: 'Form',
            children: [{
              value: 'radio',
              label: 'Radio 单选框'
            }, {
              value: 'checkbox',
              label: 'Checkbox 多选框'
            }, {
              value: 'input',
              label: 'Input 输入框'
            }, {
              value: 'input-number',
              label: 'InputNumber 计数器'
            }, {
              value: 'select',
              label: 'Select 选择器'
            }, {
              value: 'cascader',
              label: 'Cascader 级联选择器'
            }, {
              value: 'switch',
              label: 'Switch 开关'
            }, {
              value: 'slider',
              label: 'Slider 滑块'
            }, {
              value: 'time-picker',
              label: 'TimePicker 时间选择器'
            }, {
              value: 'date-picker',
              label: 'DatePicker 日期选择器'
            }, {
              value: 'datetime-picker',
              label: 'DateTimePicker 日期时间选择器'
            }, {
              value: 'upload',
              label: 'Upload 上传'
            }, {
              value: 'rate',
              label: 'Rate 评分'
            }, {
              value: 'form',
              label: 'Form 表单'
            }]
          }, {
            value: 'data',
            label: 'Data',
            children: [{
              value: 'table',
              label: 'Table 表格'
            }, {
              value: 'tag',
              label: 'Tag 标签'
            }, {
              value: 'progress',
              label: 'Progress 进度条'
            }, {
              value: 'tree',
              label: 'Tree 树形控件'
            }, {
              value: 'pagination',
              label: 'Pagination 分页'
            }, {
              value: 'badge',
              label: 'Badge 标记'
            }]
          }, {
            value: 'notice',
            label: 'Notice',
            children: [{
              value: 'alert',
              label: 'Alert 警告'
            }, {
              value: 'loading',
              label: 'Loading 加载'
            }, {
              value: 'message',
              label: 'Message 消息提示'
            }, {
              value: 'message-box',
              label: 'MessageBox 弹框'
            }, {
              value: 'notification',
              label: 'Notification 通知'
            }]
          }, {
            value: 'navigation',
            label: 'Navigation',
            children: [{
              value: 'menu',
              label: 'NavMenu 导航菜单'
            }, {
              value: 'tabs',
              label: 'Tabs 标签页'
            }, {
              value: 'breadcrumb',
              label: 'Breadcrumb 面包屑'
            }, {
              value: 'dropdown',
              label: 'Dropdown 下拉菜单'
            }, {
              value: 'steps',
              label: 'Steps 步骤条'
            }]
          }, {
            value: 'others',
            label: 'Others',
            children: [{
              value: 'dialog',
              label: 'Dialog 对话框'
            }, {
              value: 'tooltip',
              label: 'Tooltip 文字提示'
            }, {
              value: 'popover',
              label: 'Popover 弹出框'
            }, {
              value: 'card',
              label: 'Card 卡片'
            }, {
              value: 'carousel',
              label: 'Carousel 走马灯'
            }, {
              value: 'collapse',
              label: 'Collapse 折叠面板'
            }]
          }]
        }, {
          value: 'ziyuan',
          label: '资源',
          children: [{
            value: 'axure',
            label: 'Axure Components'
          }, {
            value: 'sketch',
            label: 'Sketch Templates'
          }, {
            value: 'jiaohu',
            label: '组件交互文档'
          }]
        }
      ],
      method: {
        handleSwitch(row, index) {
          console.log(index)
        }
      }
    }
  },
  methods: {
    getDate() {
      var that = this
      const path = 'http://127.0.0.1:5000/asset/network'
      axios.get(path).then(function(response) {
        var msg = response.data.msg
        that.hostgroup = msg
      })
    }
  }
}
</script>
