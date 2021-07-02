<template>
    <div class="gupiao-analysis">
        <el-collapse v-model="activeNames">
            <el-collapse-item :name="i" v-for="(item, i) in model">
                <template slot="title" class="collapse-title">
                    <span>{{item.title}}</span>
                    <image-preview v-if="item.smallImg" :imgUrl="item.smallImg" :setStyle="getStyle"></image-preview>
                </template>
                <div class="gupiao-analysis--content">
                    <div>
                        <div class="size16 title">说明：</div>
                        <div class="red textIndent">{{item.desc}}</div>
                    </div>
                    <div v-if="item.mainImg"><image-preview :imgUrl="item.mainImg" ></image-preview></div>
                    <div v-if="item.conditions">
                        <div class="size16 title">条件：</div>
                        <p class="textIndent" v-for="(condition, k) in item.conditions">{{condition}}</p>
                    </div>
                    
                    <div v-if="item.example">
                        <div class="size16 title">例子：</div>
                        <div class="margin50100 box1297e4" v-for="(img, k) in item.example"><image-preview :imgUrl="img" ></image-preview></div>
                    </div>
                    
                    <div v-if="item.remark">
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
                activeNames: ['0'],
                // example 的图片高度尺寸 控制在300px以内，最好230左右
                model: [
                    {
                        title: '亢龙有悔（大盘，日线）',
                        smallImg: 'gupiao/亢龙有悔/logo.png',
                        desc: '大盘模型',
                        mainImg: 'gupiao/亢龙有悔/klyh.png',
                        conditions: ['第一天的阴线尽量小', '第二天的阴线尽量大', '第三天的阳线要低开高收'],
                        example: ['gupiao/亢龙有悔/example1.png'],
                        remark: `
                        `
                    },
                    {
                        title: '半价次新股',
                        desc: '次新股 下跌至一半的价格，或继续下跌至33%的价位',
                        conditions: ['最开始的一字涨停板到第一波最高点后下跌，等待到50%的位置再观察是否还将继续下跌', '半价买入或者底部直接买入，盈利20%'],
                         remark: `
                        `
                    },
                    {
                        title: '七星落长空 - I型（个股，日线）',
                        smallImg: 'gupiao/七星/七星-1-img.png',
                        desc: '下跌趋势中的底部模型',
                        mainImg: 'gupiao/七星/七星-1.png',
                        conditions: ['1. 阴阳线的真、假都可以(*①)', '2. 阴阳线的大、小都行', '3. 阴阳线的高低开都可以', '4. 下跌趋势中，基本都在底部'],
                        example: ['gupiao/七星/example1-1.png', 'gupiao/七星/example12-1.png'],
                        remark: `
                        `
                    },
                    {
                        title: '七星落长空 - II型（个股，日线）',
                        smallImg: 'gupiao/七星/七星-2-img.png',
                        desc: '下跌趋势中的底部模型',
                        mainImg: 'gupiao/七星/七星-2.png',
                        example: ['gupiao/七星/example12-1.png', 'gupiao/七星/example2-1.png', 'gupiao/七星/example2-2.png'],
                        conditions: ['阴阳线的真、假都可以', '阴阳线的大、小都行', '阴阳线的高低开都可以', '4. 下跌趋势中，基本都在底部'],
                        remark: ''
                    },
                    {
                        title: '价格中枢1（个股，周线）',
                        smallImg: 'gupiao/价格中枢/logo.png',
                        desc: '下跌后的筑底',
                        mainImg: 'gupiao/价格中枢/jgzs.png',
                        example: ['gupiao/价格中枢/example1.png', 'gupiao/价格中枢/example2.png', 'gupiao/价格中枢/example3.png', 'gupiao/价格中枢/example4.png', 'gupiao/价格中枢/example5.png', 'gupiao/价格中枢/example6.png'],
                        remark: `
                        `
                    },
                    {
                        title: '价格中枢2（个股，周线）',
                        smallImg: 'gupiao/价格中枢/logo2.png',
                        desc: '上涨初期或中期',
                        mainImg: 'gupiao/价格中枢/jgzs2.png',
                        example: ['gupiao/价格中枢/example2-1.png', 'gupiao/价格中枢/example2-2.png'],
                        remark: `
                        `
                    },
                    {
                        title: '看跌阴线3（个股，周线）',
                        smallImg: 'gupiao/价格中枢/看跌阴线/logo3.png',
                        desc: '上涨的末期',
                        mainImg: 'gupiao/价格中枢/看跌阴线/kdyx3.png',
                        example: ['gupiao/价格中枢/看跌阴线/example3-1.png', 'gupiao/价格中枢/看跌阴线/example3-2.png', 'gupiao/价格中枢/看跌阴线/example3-3.png'],
                        remark: `
                        `
                    },
                    {
                        title: '看涨阴线4（个股，周线）',
                        smallImg: 'gupiao/价格中枢/看跌阴线/logo4.png',
                        desc: '下跌后的筑底',
                        mainImg: 'gupiao/价格中枢/看跌阴线/kdyx4.png',
                        example: ['gupiao/价格中枢/看跌阴线/example4-1.png', 'gupiao/价格中枢/看跌阴线/example4-2.png', 'gupiao/价格中枢/看跌阴线/example4-3.png'],
                        remark: `
                        `
                    },
                    {
                        title: '上涨诱空大阴线抄底（个股，日线）',
                        smallImg: 'gupiao/诱空抄底/logo.png',
                        desc: '上涨途中的追涨抢跑',
                        mainImg: 'gupiao/诱空抄底/szjgcddwykdyx.png',
                        example: ['gupiao/诱空抄底/example.png', 'gupiao/诱空抄底/example2.png', 'gupiao/诱空抄底/example3.png', 'gupiao/诱空抄底/example4.png'],
                        remark: `
                        `
                    },
                    {
                        title: '否极泰来',
                        smallImg: 'gupiao/否极泰来/logo.png',
                        desc: '真正的底部模型',
                        mainImg: 'gupiao/否极泰来/pjtl.png',
                        example: ['gupiao/否极泰来/example1.png', 'gupiao/否极泰来/example2.png'],
                        remark: `
                        `
                    },
                    {
                        title: '飞龙在天',
                        smallImg: 'gupiao/飞龙在天/logo.png',
                        desc: '大盘好的时候用，超短期追涨停，80%胜率',
                        mainImg: 'gupiao/飞龙在天/flzt.png',
                        // example: ['gupiao/飞龙在天/example1.png', 'gupiao/飞龙在天/example2.png'],
                        remark: ``
                    },
                    {
                        title: '神龙摆尾-zero（个股，日线）',
                        smallImg: 'gupiao/神龙摆尾0/logo.png',
                        desc: '急速下跌/熊市末期',
                        mainImg: 'gupiao/神龙摆尾0/slbw0.png',
                        example: ['gupiao/神龙摆尾0/example1.png', 'gupiao/神龙摆尾0/example2.png', 'gupiao/神龙摆尾0/example3.png'],
                        remark: `
                        `
                    },
                    {
                        title: '神龙摆尾1（个股，日线）',
                        smallImg: 'gupiao/神龙摆尾1/logo.png',
                        desc: '筑底后震荡的第一个涨停板',
                        mainImg: 'gupiao/神龙摆尾1/slbw1.png',
                        example: ['gupiao/神龙摆尾1/example1.png', 'gupiao/神龙摆尾1/example2.png'],
                        remark: `
                        `
                    },
                    {
                        title: '神龙摆尾3（个股，日线）',
                        smallImg: 'gupiao/神龙摆尾3/logo.png',
                        desc: '筑底后震荡的第一个涨停板',
                        mainImg: 'gupiao/神龙摆尾3/slbw.png',
                        example: ['gupiao/神龙摆尾3/example1.png', 'gupiao/神龙摆尾3/example2.png', 'gupiao/神龙摆尾3/example3.png'],
                        remark: `
                        `
                    },
                    {
                        title: '反客为主（个股，日线）',
                        smallImg: 'gupiao/反客为主/logo.png',
                        desc: '上涨结构(*②)中的某个位置',
                        mainImg: 'gupiao/反客为主/fkww.png',
                        example: ['gupiao/反客为主/example1.png']
                    },
                    {
                        title: '峰回路转（个股，日线）',
                        smallImg: 'gupiao/峰回路转/logo.png',
                        desc: '上涨结构的主力洗盘',
                        mainImg: 'gupiao/峰回路转/fhlz.png',
                        example: ['gupiao/峰回路转/example1.png'],
                        remark: `
                        `
                    },
                    {
                        title: '以逸待劳（个股，日线）',
                        smallImg: 'gupiao/以逸待劳/logo.png',
                        desc: '底部的主力洗盘',
                        mainImg: 'gupiao/以逸待劳/yydl.png',
                        example: ['gupiao/以逸待劳/example1.png', 'gupiao/以逸待劳/example2.png'],
                        remark: `
                        `
                    },
                    {
                        title: '出水芙蓉（个股，日线）',
                        smallImg: 'gupiao/出水芙蓉/logo.png',
                        desc: '主力低位洗盘模型，大盘比较弱的时候用',
                        mainImg: 'gupiao/出水芙蓉/csfr.png',
                        example: ['gupiao/出水芙蓉/example1.png', 'gupiao/出水芙蓉/example2.png', 'gupiao/出水芙蓉/example3.png'],
                        remark: `
                        `
                    },
                    {
                        title: '一箭双雕（个股，日线）',
                        smallImg: 'gupiao/一箭双雕/logo.png',
                        desc: '中继加速模型，主力拉升前的洗盘',
                        mainImg: 'gupiao/一箭双雕/yjsd.png',
                        example: ['gupiao/一箭双雕/example1.png', 'gupiao/一箭双雕/example2.png', 'gupiao/一箭双雕/example3.png'],
                        remark: `
                        `
                    },
                    {
                        title: '柳暗花明（个股，日线）',
                        smallImg: 'gupiao/柳暗花明/logo.png',
                        desc: '底部反转模型，主力底部的强势洗盘',
                        mainImg: 'gupiao/柳暗花明/lahm.png',
                        // example: ['gupiao/柳暗花明/example1.png', 'gupiao/柳暗花明/example2.png', 'gupiao/柳暗花明/example3.png'],
                        remark: `
                        `
                    },
                    {
                        title: '葛式八法 - 买2（个股，周日线）',
                        smallImg: 'gupiao/葛式八法/logo2.png',
                        
                        mainImg: 'gupiao/葛式八法/买2.png',
                        example: ['gupiao/葛式八法/example2-1.png', 'gupiao/葛式八法/example2-2.png'],
                        remark: `
                        `
                    },
                    {
                        title: '神奇均线（个股，日线）',
                        smallImg: 'gupiao/神奇均线/logo.png',
                        // desc: '',
                        mainImg: 'gupiao/神奇均线/sqjx.png',
                        example: ['gupiao/神奇均线/example1.png', 'gupiao/神奇均线/example2.png'],
                        remark: `
                        `
                        
                    },
                    {
                        title: '鱼跃龙门（个股，月线）',
                        smallImg: 'gupiao/鱼跃龙门/logo.png',
                        // desc: '',
                        mainImg: 'gupiao/鱼跃龙门/yylm.png',
                        example: ['gupiao/鱼跃龙门/example1.png', 'gupiao/鱼跃龙门/example2.png'],
                        remark: `
                        `
                        
                    },
                    {
                        title: '隔山打牛（个股，日线）',
                        smallImg: 'gupiao/隔山打牛/logo.png',
                        desc: '上涨初期或中期',
                        mainImg: 'gupiao/隔山打牛/gsdn.png',
                        example: ['gupiao/analysis/'],
                        remark: `
                        `
                        
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
            },
            getItem() {
                return item => {
                    
                }
            }
        }
    }
</script>

<style lang="less" scoped>
.gupiao-analysis {
    /deep/ .el-collapse-item__content {
        padding: 10px;
    }
    .el-collapse-item__header {
        display: flex;
        .image-preview {
            flex: 1;
            text-align: right;
            margin: 0 10px;
            padding-right: 10px;
        }
    }
    .gupiao-analysis--content {
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