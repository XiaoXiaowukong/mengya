<template>
  <div class="videoItem" :videoDataSingle="videoDataSingle">
    <div class="caseItem" v-for="(img_item,index) in videoDataSingle" :key="index">
      <div v-if="index > 0" class="caseLeft">
        <img :src="img_item.img_file">
      </div>
      <div v-else>
        <img :src="img_item.img_file">
      </div>
      <p>{{img_item.title}}</p>
      <p>{{img_item.content}}</p>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "ComponentVideoItem",
    props: {
      videoDataSingle: {
        type: Array,
        default: () => []
      }
    }
  }
</script>

<style scoped>
  .videoItem {
    text-align: center;
  }

  .videoItem img {
    width: 400px;
    height: 300px;
  }

  .caseItem {
    display: inline-block;
  }

  .caseLeft {
    padding-left: 5px;
  }

  .caseItem p {
    font-size: 8px;
    text-align: left;
    padding-left: 5px;
  }
</style>
