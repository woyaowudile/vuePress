<template>
    <div class="vant">
        <van-image
            fit="cover"
            :src="url12"
            @click="clickPreview(url12)"
        />
        <van-image-preview
            v-model="show"
            :images="images"
            >
            <template v-slot:index>第{{ index }}页</template>
        </van-image-preview>
    </div>
</template>

<script>
    export default {
        props: {
            imgUrl: {
                type: String,
                default: ''
            }
        },
        data() {
            return {
                show: false,
                images: [],
                index: 1,
                // url12: require(this.imgUrl)
                url12: require(`./../statcs/${this.imgUrl}`)
            }
        },
        methods: {
            clickPreview(url) {
                this.show = true
                this.images = [url]
            }
        }
    }
</script>

<style lang="less" scoped>

</style>