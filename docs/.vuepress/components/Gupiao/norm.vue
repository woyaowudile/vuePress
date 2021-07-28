<template>
    <div class="gupiao-norm">
        <el-row>
            <el-col :span="24">
                <el-collapse v-model="activeNames">
                    <el-collapse-item v-for="(v, k) in Object.keys(items)" :title="names[k]" :name="k">
                        <div id="box" v-for="(item, i) in items[v]" :key="i">
                            <h4 v-if="item.pTitle">{{item.pTitle}}</h4>
                            <div v-for="(level1, index1) in item.list" :key="index1 + '0'" class="flexbox lh40">
                                <span>{{level1.content}}</span>
                                <el-popover
                                    v-if="level1.title"
                                    class="flex1 tar"
                                    trigger="click"
                                    placement="bottom"
                                    width="350"
                                    :title="level1.title"
                                    >
                                    <div v-html="level1.desc"></div>
                                    <el-button type="text"  slot="reference">查看详情</el-button>
                                </el-popover>
                            </div>
                            <div class="dispalyinlineBlock flexbox" v-if="item.smallImgs.length" v-for="(level1, index1) in item.smallImgs" :key="index1+'1'">
                                <image-preview :imgUrl="level1" :setStyle="getStyle"></image-preview>
                            </div>
                        </div>
                        <!-- <div>
                            <div>11111111</div>
                            <p>2. 柱体</p>
                        </div> -->
                    </el-collapse-item>
                </el-collapse>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                activeNames: [],
                names: ['指标说明', '买入', '卖出'],
                items: {
                    desc: [
                        {
                            list: [
                                {
                                    title: '指标说明',
                                    content: 'MACD参数越大，变化慢，越稳定',
                                    desc: `
                                        <div><span style="color:red">EMA</span>： 快8， 慢13</div>
                                        <div><span style="color:red">DIF</span>： 9</div>
                                        <div><span style="color:red">MA</span>： 5,10,30</div>
                                    `
                                },
                                {
                                    title: '红绿柱法则',
                                    content: '红绿柱法则',
                                    desc: `
                                        <div>0轴上要3天，0轴下也要3天。是中短期</div>
                                        <div>下跌3次后，有买点可进场</div>
                                        <div>上涨3次后，有卖点 必卖</div>
                                        <div>在此期间，红/绿柱持续时间越长，未来涨/跌越大</div>
                                    `
                                }
                            ]
                        }
                    ],
                    buy: [
                        {
                            pTitle: '1. 双线',
                            list: [
                                {
                                    title: '金叉',
                                    content: '金叉： DIF 上穿 DEA',
                                    desc: `
                                        <div><span style="color:red">1. 0轴上方： 强势金叉。股市强势中，可加仓或持股待涨</span></div>
                                        <div>一般是前面出现了一波金叉，这两个金叉，要么前面涨幅大，要么后面涨幅大</div>
                                        <div><span style="color:red">2. 0轴附近： 强势金叉。中长线买入信号</span></div>
                                        <div>① 底部小幅上升后，横盘一段短时间，放量突破</div>
                                        <div>② 底部大段涨幅，长时间中位回档整理，然后股价向上、MACD金叉</div>
                                        <div><span style="color:red">3. 0轴下方： 弱势金叉。由弱转强，可买进或持股，并不表示下跌也结束</span></div>
                                        <div>双线同时向上靠近0轴，若红柱开始放出（尤其二次放出）。下跌趋势已结束</div>
                                    `
                                },
                                {
                                    title: '柱线分析',
                                    content: '柱线分析',
                                    desc: `
                                        <div>0轴上方时，红柱又二次翻红，即红柱由大变小，再次变大</div>
                                        <div>0轴下方时，绿柱低位运行一段时间，慢慢收缩变红。但中长期下跌趋势并没有完全改变</div>
                                    `
                                }
                            ],
                            smallImgs: ['gupiao/四大天王/MACD/双线-金叉-2-1.png', 'gupiao/四大天王/MACD/双线-金叉-2-2.png']
                        },
                        {
                            pTitle: '2. 柱体',
                            list: [
                                {
                                    title: '红柱',
                                    content: '红柱持续放大，或绿转红',
                                    desc: `
                                        <div><span style="color:red">红柱持续放大</span>：可短期买入。无法放大时，再考虑卖出</div>
                                        <div><span style="color:red">绿->红</span>：下跌或低位盘整已结束，加仓买入待涨 </div>
                                        <div><span style="color:red">绿柱收缩</span>：大跌行情即将结束，可布局长线，不轻易卖出</div>
                                    `
                                }
                            ]
                        },
                        {
                            pTitle: '3. 底背离',
                            list: [
                                {
                                    title: '底背离',
                                    content: 'k线走低， DIF走高',
                                    desc: `
                                        <div><span style="color:red">底背离需要多次确认</span></div>
                                    `
                                }
                            ]
                        },
                        {
                            pTitle: '4. 多周期共振法则',
                            list: [
                                {
                                    title: '周期共振',
                                    content: '月周、日、60和30分钟、15和5分钟',
                                    desc: `
                                        <div><span style="color:red">含义：至少两个周期都出现买卖点</span></div>
                                        <div>如果月周出现买卖点，其他周期也出现。说明后市力度大，可重仓</div>
                                        <div>短线则使用后面两个周期来判断</div>
                                        <div>不必都是MACD，其他指标也可以</div>
                                    `
                                }
                            ]
                        }
                    ],
                    sale: [
                        {
                            pTitle: '1. 双线',
                            list: [
                                {
                                    title: '死叉',
                                    content: '死叉： DIF 下穿 DEA',
                                    desc: `
                                        <div><span style="color:red">0轴上方</span>： 强转弱，大跌。只能卖不能买</div>
                                        <div><span style="color:red">0轴下方</span>： 进入极度弱势，还将下跌， 卖出或观望</div>
                                    `
                                }
                            ]
                        },
                        {
                            pTitle: '2. 柱体',
                            list: [
                                {
                                    title: '绿柱',
                                    content: '绿柱持续放大，或红柱缩小，或绿转红',
                                    desc: `
                                        <div><span style="color:red">绿柱放大</span>：股价继续下跌，应观望或卖出</div>
                                        <div><span style="color:red">红->绿</span>：上涨或高位盘整已结束，不能买入，且需卖出所有或大部分 </div>
                                        <div><span style="color:red">红柱收缩</span>：将大幅下跌，不能买入，只能卖出</div>
                                    `
                                },
                            ]
                        },
                        {
                            pTitle: '3. 顶背离',
                            list: [
                                {
                                    title: '顶背离',
                                    content: 'k线走高， DIF走低',
                                    desc: `
                                        <div><span style="color:red">顶背离准确性要大于底背离</span></div>
                                    `
                                }
                            ]
                        },
                        {
                            pTitle: '4. 第一卖点',
                            list: [
                                {
                                    title: '第一卖点',
                                    content: '大幅拉升后要横盘，而形成的一个相对高点',
                                    desc: `
                                        <div><span style="color:red">MACD死叉，5、10均线还未死叉</span></div>
                                        <div>均线死叉后卖出或减仓</div>
                                    `
                                }
                            ]
                        },
                        {
                            pTitle: '5. 绝对顶',
                            list: [
                                {
                                    title: '绝对顶',
                                    content: '主力出货前的最后一次拉升，又称虚浪拉升',
                                    desc: `
                                        <div>第一卖点形成后，没有大跌，而是在回调掩护出货假装向上突破</div>
                                        <div><span style="color:red">研判标准：</span>虚浪拉升创新高，但MACD没创新高。见顶的明显信号</div>
                                        <div><span style="color:red">但不能等MACD死叉后再卖</span></div>
                                        <div><span style="color:red">最佳时机：</span>高开低走的阴线，长下影线涨停阳线</div>

                                    `
                                }
                            ]
                        }
                    ]
                }
            }
        },
        computed: {
            getStyle() {
                return {
                    'width': '50px',
                    'margin-left': '10px !important',
                    'vertical-align': 'middle'
                }
            }
        }
    }
</script>

<style lang="less" scoped>
.gupiao-norm {
    .image-preview {
        display: inline-block;
        border-radius: 2px;
        box-shadow: 0 0 5px 0px #e19494;
    }
    .dispalyinlineBlock {
        display: inline-block;
        margin: 0 5px !important;
    }
}
.flexbox {
    display: flex;
}
.flex1 {
    flex: 1;
}
.tar {
    text-align: right;
    line-height: 40px;
}
.lh40 {
    line-height: 40px;
}
#box {
    // class权重不够 */
    margin: 10px 4px!important;
    padding: 5px;
    box-shadow: 0px 0px 2px 2px #d4c8c8;
    border-radius: 5px;
}
</style>