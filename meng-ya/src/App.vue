<template>
  <div class="app">
    <div class="headWrapper">
      <div class="container">
        <img class="logo" src="./assets/logo.png"/>
        <ul class="nav">
          <li class="nav-item">
            <router-link :to="{name: 'home'}" class="active_item" exact>首页</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{name: 'custom'}" class="active_item">自定义</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{name: 'about'}" class="active_item">关于</router-link>
          </li>
        </ul>
        <div class="user">
          <div class="nikeName">小小悟空</div>
          <img src="./assets/logo.png"/>
        </div>
      </div>
    </div>
    <div class="contentView">
      <router-view></router-view>
    </div>
    <div class="footer">
      <div class="firendLink" v-for="(first_item,index) in first_array" :key="index">
        <p>{{first_item}}</p>
      </div>
      <div class="footer_support">
        <p>技术支持:山西微众科技有限公司</p>
      </div>
    </div>

  </div>
</template>
<script>
/* eslint-disable */
  export default {
    data() {
      return {
        first_array: ["友情链接：www.baidu.com", "友情链接：www.baidu.com"]
      };
    }
  }
</script>
<style lang="less">
  html, body {
    margin: 0;
    padding: 0;
  }

  .app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  .headWrapper {
    height: 80px;
    position: fixed;
    width: 100%;
    left: 0;
    top: 0;
    z-index: 1500;
    display: block;
    background: #ffffff;
  }

  .container {
    height: 100%;
    box-sizing: border-box;
    border-bottom: 1px solid #dcdfe6;
    width: 1140px;
    margin: 0 auto;
  }

  .nav {
    height: 100%;
    line-height: 80px;
    background: transparent;
    margin: 0;
    display: inline-block
  }

  .nav-item {
    margin: 0;
    padding-left: 10px;
    float: left;
    list-style: none;
    position: relative;
    cursor: pointer;
  }

  .logo {
    float: left;
    padding-top: 15px;
    padding-left: 30px;
    width: 50px;
    height: 50px;
    display: inline-block
  }

  .user {
    float: right;
    height: 100%;
    margin: 0;
    padding-right: 20px;
  }

  .user img {
    padding-top: 25px;
    width: 30px;
    height: 30px;
    display: inline-block
  }

  .nikeName {
    padding-right: 10px;
    display: inline-block
  }

  .active_item {
    font-size: 20px;
    color: #358ee7;
  }

  .contentView {
    width: 100%;
  }

  .footer {
    width: 100%;
    height: 200px;
    background: #2c3e50;
    position: relative;
    text-align: center;
  }

  .firendLink {
    display: inline-block;
  }

  .firendLink p {
    font-size: 10px;
    color: white;
    display: inline-block;
  }
  .footer_support {
  }
  .footer_support p{
    color: white;
    font-size: 10px;
    padding-top: 100px;
  }

</style>
