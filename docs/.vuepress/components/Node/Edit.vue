<template>
    <div>
        <div id="node-edit" @focus="editFoucs" @blur="editBlur" contenteditable="true">
            点击以编辑(必须要分号)...
        </div>
        <div id="box"></div>
        <div id="btn-box">
            <van-button class="btn" type="primary" @click="btnClick">主要按钮</van-button>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                eidtAfterWord: '点击以编辑(必须要分号)...'
            }
        },
        computed: {
            dom() {
                return document && document.getElementById('node-edit')
            }
        },
        methods: {
            editBlur(e) {
                let value = e.target.textContent
                this.eidtAfterWord = this.dom.innerHTML = value
            },
            editFoucs() {
                this.dom.innerHTML = this.eidtAfterWord
            },
            btnClick() {
                // 拿到编辑框中输入的字符串
                eval(this.eidtAfterWord)
            }
        }
    }
</script>

<style lang="less" scoped>
#node-edit {
    padding: 20px;
    border: 1px dashed #f1f1f1;
    margin: 10px 0 !important;
    &:focus {
        border: 1px solid red;
    }
}
.btn-box {
    text-align: right;
    /deep/ .btn {
        border-radius: 10px;
    }
}
</style>