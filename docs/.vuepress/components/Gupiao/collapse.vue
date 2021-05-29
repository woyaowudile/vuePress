<template>
    <div class="gupiao-collapse">
        <el-collapse v-model="activeNames">
            <el-collapse-item :name="i" v-for="(item, i) in model">
                <template slot="title">
                    <span>{{item.title}}</span>
                    <image-preview :imgUrl="item.smallImg" :setStyle="getStyle"></image-preview>
                </template>
                <div class="gupiao-collapse--content">
                    <div>
                        <div class="size16 title">说明：</div>
                        <div class="red textIndent">{{item.desc}}</div>
                    </div>
                    <div><image-preview :imgUrl="item.mainImg" ></image-preview></div>
                    <div>
                        <div class="size16 title">条件：</div>
                        <p class="textIndent" v-for="(condition, k) in item.conditions">{{condition}}</p>
                    </div>
                    
                    <div>
                        <div class="size16 title">例子：</div>
                        <div class="margin50100 box1297e4" v-for="(img, k) in item.example"><image-preview :imgUrl="img" ></image-preview></div>
                    </div>
                    
                    <div>
                        <div class="size16 title">备注：</div>
                        <!-- <el-input
                            type="textarea"
                            disabled
                            placeholder="请输入内容"
                            v-model="item.remark">
                        </el-input> -->
                        <div class="textIndent" v-html="item.remark"></div>
                    </div>
                </div>
            </el-collapse-item>
        </el-collapse>
    </div>
</template>

<script>
    import imagePreview from '../image-preview.vue'
    export default {
        components: { imagePreview },
        data() {    
            return {
                activeNames: ['1'],
                // example 的图片高度尺寸 控制在300px以内，最好230左右
                model: [
                    {
                        title: '七星落长空 - I型(个股，日线)',
                        smallImg: 'gupiao/七星/七星-1-img.png',
                        desc: '下跌趋势中的底部模型',
                        mainImg: 'gupiao/七星/七星-1.png',
                        conditions: ['1. 阴阳线的真、假都可以(*①)', '2. 阴阳线的大、小都行', '3. 阴阳线的高低开都可以', '4. 下跌趋势中，基本都在底部'],
                        example: ['gupiao/七星/example1-1.png', 'gupiao/七星/example12-1.png'],
                        remark: `<a href="https://live.study.163.com/live/index.html?courseId=100080957&lesson=103776758&type=1">1. 第一阶段 -> 短线抄底模型 -> 2、3课 </a>
                            <div>2. 无论 I型 还是 II型，都是短线抄底模型，见好就收，不要拿着不放</div>
                        `
                    },
                    {
                        title: '七星落长空 - II型(个股，日线)',
                        smallImg: 'gupiao/七星/七星-2-img.png',
                        desc: '下跌趋势中的底部模型',
                        mainImg: 'gupiao/七星/七星-2.png',
                        example: ['gupiao/七星/example12-1.png', 'gupiao/七星/example2-1.png', 'gupiao/七星/example2-2.png'],
                        conditions: ['阴阳线的真、假都可以', '阴阳线的大、小都行', '阴阳线的高低开都可以', '4. 下跌趋势中，基本都在底部'],
                        remark: '无论 I型 还是 II型，都是短线抄底模型，见好就收，不要拿着不放'
                    },
                ]
            }
        },
        computed: {
            getStyle() {
                return {
                    'width': '80px',
                    'margin-left': '10px !important',
                    'vertical-align': 'middle'
                }
            }
        }
    }
</script>

<style lang="less" scoped>
.gupiao-collapse {
    /deep/ .el-collapse-item__content {
        padding: 10px;
    }
    .gupiao-collapse--content {
        box-shadow: 1px 1px 8px;
        padding: 5px 10px;
        border-radius: 5px;
        max-height: 300px;
        overflow: auto;
                
        .margin50100 {
            margin: 5px 0 10px 0 !important;
        }
    }
}
.red {
    color: red
}
.size16 {
    font-size: 16px;
}
.title {
    background: #eee;
    padding: 2px 10px;
}
.textIndent {
    text-indent: 2em;
}
.box1297e4 {
    box-shadow: 1px 1px 4px 0px #1297e4;
}
</style>