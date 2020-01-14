<template>
  <div class="videoItem" :videoDataSingle="videoDataSingle">
    <h4>{{videoDataSingle.title}}</h4>
    <div class="img_clss" v-for="(img_item,index) in videoDataSingle.img_files" :key="index">
      <img :src="img_item">
    </div>
    <p>{{videoDataSingle.content}}</p>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: "ComponentHomeCase",
    props: {
      videoDataSingle: {
        type: Object,
        default: () => {
        }
      }
    }
  }
</script>

<style scoped>
  .videoItem {
    padding-left: 200px;
  }

  .videoItem img {
    width: 100px;
    height: 100px;

  }

  .img_clss {
    display: inline-block;
    padding: 5px;
  }
</style>
