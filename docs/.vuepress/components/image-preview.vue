<template>
  <div class="image-preview">
    <van-image
      fit="cover"
      :heght="height || '100%'"
      :width="width || '100%'"
      :style="setStyle"
      :src="getUrl"
      @click="clickPreview(getUrl)"
    />
    <van-image-preview
      v-model="show"
      :images="images"
      @click.native="clickShow"
    >
      <template v-slot:index>第{{ index }}页</template>
    </van-image-preview>
    <!-- <Modal title="View Image" v-model="show">
      <img :src="images" v-if="show" style="width: 100%" />
    </Modal> -->
  </div>
</template>

<script>
export default {
  inject: ["env"],
  props: {
    imgUrl: {
      type: String,
      default: "",
    },
    setStyle: {
      type: Object,
      default: () => {},
    },
    width: {
      type: String,
      default: "",
    },
    height: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      show: false,
      images: [],
      index: 1,
    //   url12: isProduction ? `${this.env?.url}${this.imgUrl}` :  require(`${this.env?.url}${this.imgUrl}`),
      //   url12: require(`./../statcs/${this.imgUrl}`)
    };
  },
  computed: {
      isProduction() {
          return ['production', 'prod'].includes(process.env.NODE_ENV)
      },
      getUrl() {
        //   require 必须使用明确的地址前缀，不能用变量替代
           return this.isProduction ? `${this.env?.url}${this.imgUrl}` :  require(`./../statcs${this.env?.url}${this.imgUrl}`)
      }
  },
  methods: {
    clickPreview(url) {
      this.show = true;
      this.images = [url];
    },
    clickShow() {
      this.show = false;
    },
  },
};
</script>
