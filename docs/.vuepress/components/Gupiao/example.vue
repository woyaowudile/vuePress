<template>
    <div class="gp-example">
         <el-button type="text" @click="click">{{name}}</el-button>

        <el-dialog
            class="gp-example--dialog"
            :title="dialog.title"
            :visible.sync="dialog.visible"
            width="100%">
            <div>
                <el-collapse>
                    <el-collapse-item name="2">
                        <div slot="title">
                            失败
                        </div>
                        <image-preview :imgUrl="getImgUrl" width="200"></image-preview>
                    </el-collapse-item>
                    <el-collapse-item name="3">
                        <div slot="title">
                            成功
                        </div>
                        <image-preview :imgUrl="getImgUrl" width="200"></image-preview>
                    </el-collapse-item>
                </el-collapse>
            </div>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialog.visible = false">取 消</el-button>
            </span>
        </el-dialog>

    </div>
</template>

<script>
import imagePreview from '../image-preview.vue'
    export default {
        name: 'gp-example',
        components: { imagePreview },
        props: {
            name: String
        },
        data() {
            return {
                dialog: {
                    visible: false,
                    title: '提示'
                }
            }
        },
        computed: {
            getImgUrl() {
                return 'gupiao/亢龙有悔/example1.png'
            }
        },
        methods: {
            click() {
                this.dialog.visible = true
            }
        }
    }
</script>

<style lang="less" scoped>
.gp-example {
    .gp-example--dialog {
        max-height: 100vh;
        // /deep/ .el-dialog {

        //     left: 50%;
        //     transform: translateX(-50%);
        //     margin-top: 15vh !important;
        // }
    }
}
</style>