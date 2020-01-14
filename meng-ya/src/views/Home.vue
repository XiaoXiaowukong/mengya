<template>
  <div>
    <img class="banner" src="../assets/banner1.jpg">
    <div class="workType">
      <div>
        <img src="../assets/women1.jpg"/>
        <h2>测试1</h2>
      </div>
      <div class="workItem">
        <img src="../assets/women2.jpg"/>
        <h2>测试2</h2>
      </div>
      <div class="workItem">
        <img src="../assets/women3.jpg"/>
        <h2>测试3</h2>
      </div>
      <div class="workItem">
        <img src="../assets/women4.jpg"/>
        <h2>测试4</h2>
      </div>
    </div>
    <div v-for="(case_item ,index ) in videoData.case" :key="index">
      <home-case :videoDataSingle="case_item"></home-case>

    </div>
  </div>
</template>

<script>
/* eslint-disable */
  import homeCase from "../components/ComponentHomeCase"
  import {getActivityList} from "@/api/common"

  export default {
    name: "home",
    components: {
      homeCase
    },
    data() {
      return {
        videoData: [],
        ared_id: 100
      };
    },
    mounted() {
      this.setActivityList();
    },
    methods: {
      // 逐时次
      async setActivityList() {
        const res = await getActivityList({
          ared_id: this.ared_id,
        });
        this.videoData = res.data;
      }
    }
  }
</script>
<style>
  .banner {
    width: 100%;
    height: 100%;
  }

  .workType {
    padding-top: 10px;
    text-align: center
  }

  .workType div {
    display: inline-block;
  }

  .workItem {
    padding-left: 30px;
  }

</style>
