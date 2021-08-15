<template>
    <div class="gupiao-collapse">
        <el-collapse v-model="activeNames">
            <el-collapse-item :name="i" v-for="(item, i) in model">
                <template slot="title" class="collapse-title">
                    <span>{{item.title}}</span>
                    <image-preview v-if="item.smallImg" :imgUrl="item.smallImg" :setStyle="getStyle"></image-preview>
                </template>
                <div class="gupiao-collapse--content">
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
                            <div>大阴线 实体 > 小阴线 实体 的 2倍以上</div>
                            <div>止盈： 5-10日内的大阳线收盘价；任意阴线</div>
                            <div>止损： 该模型的最低价</div>
                            <div>可以多在沪深300，上证50里找</div>
                        `
                    },
                    {
                        title: '半价次新股',
                        desc: '次新股 下跌至一半的价格，或继续下跌至33%的价位',
                        conditions: ['最开始的一字涨停板到第一波最高点后下跌，等待到50%的位置再观察是否还将继续下跌', '半价买入或者底部直接买入，盈利20%'],
                         remark: `
                            <div>注意分仓、交易计划</div>
                            <div>大盘趋势不好的时候，要注意使用</div>
                        `
                    },
                    {
                        title: '七星落长空 - I型（个股，日线）',
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
                        title: '七星落长空 - II型（个股，日线）',
                        smallImg: 'gupiao/七星/七星-2-img.png',
                        desc: '下跌趋势中的底部模型',
                        mainImg: 'gupiao/七星/七星-2.png',
                        example: ['gupiao/七星/example12-1.png', 'gupiao/七星/example2-1.png', 'gupiao/七星/example2-2.png'],
                        conditions: ['阴阳线的真、假都可以', '阴阳线的大、小都行', '阴阳线的高低开都可以', '4. 下跌趋势中，基本都在底部'],
                        remark: '无论 I型 还是 II型，都是短线抄底模型，见好就收，不要拿着不放'
                    },
                    {
                        title: '看跌做涨（个股，周线）',
                        smallImg: 'gupiao/价格中枢/logo.png',
                        desc: '下跌后的筑底',
                        mainImg: 'gupiao/价格中枢/jgzs.png',
                        example: ['gupiao/价格中枢/example1.png', 'gupiao/价格中枢/example2.png', 'gupiao/价格中枢/example3.png', 'gupiao/价格中枢/example4.png', 'gupiao/价格中枢/example5.png', 'gupiao/价格中枢/example6.png'],
                        remark: `
                            低开：既可是阴线， 也可以是阳线
                            <div>如果低开后实体很大就不是</div>
                            新条件：
                            <div>收益30% - 50%</div>
                            <div>不能高开高走</div>
                            <div>第二周最好别涨上来，希望弱势些</div>
                            <div>第三周最好都是先跌后涨的(周一到周三跌，到周五涨)</div>
                        `
                    },
                    {
                        title: '看涨做涨（个股，周线）',
                        smallImg: 'gupiao/价格中枢/logo2.png',
                        desc: '上涨初期或中期',
                        mainImg: 'gupiao/价格中枢/jgzs2.png',
                        example: ['gupiao/价格中枢/example2-1.png', 'gupiao/价格中枢/example2-2.png'],
                        remark: `
                            <div>第二周高开后，确认是上涨状态，周三就可以买入</div>
                        `
                    },
                    {
                        title: '看涨阴线1（个股，周线）',
                        smallImg: 'gupiao/价格中枢/看涨阴线/logo1.png',
                        desc: '上涨途中的回调',
                        mainImg: 'gupiao/价格中枢/看涨阴线/kzyx1.png',
                        example: ['gupiao/价格中枢/看涨阴线/example1-1.png', 'gupiao/价格中枢/看涨阴线/example1-2.png'],
                        remark: `
                        <div>止损：近期最低价</div>
                        <div>第二周阳线的低开，相对于价格中枢来说</div>
                        <div>周中或下周买入</div>
                        `
                    },
                    {
                        title: '看涨阴线2（个股，周线）',
                        smallImg: 'gupiao/价格中枢/看涨阴线/logo2.png',
                        desc: '上涨途中的回调',
                        mainImg: 'gupiao/价格中枢/看涨阴线/kzyx2.png',
                        example: ['gupiao/价格中枢/看涨阴线/example2-1.png', 'gupiao/价格中枢/看涨阴线/example2-2.png', 'gupiao/价格中枢/看涨阴线/example2-3.png'],
                        remark: `
                        <div>止损：近期最低价</div>
                        <div>第二周无论高开、低开。放量、缩量 都可以</div>
                        <div>大阴线的影线： 上必需要但不能太长， 下最好没有或极短</div>
                        <div>周中或下周买入</div>
                        `
                    },
                    {
                        title: '看跌阴线3（个股，周线）',
                        smallImg: 'gupiao/价格中枢/看跌阴线/logo3.png',
                        desc: '上涨的末期',
                        mainImg: 'gupiao/价格中枢/看跌阴线/kdyx3.png',
                        example: ['gupiao/价格中枢/看跌阴线/example3-1.png', 'gupiao/价格中枢/看跌阴线/example3-2.png', 'gupiao/价格中枢/看跌阴线/example3-3.png'],
                        remark: `
                            <div>止盈： 50%+ </div>
                            <div>止损： 近期最低价 </div>
                            <div>光头不光脚(可以有一点点上影线，最好没有)</div>
                            <div>不能是锤头</div>
                            <div>不一定是最高，但一定是在高位出现的</div>
                            <div>第二周 阴线、阳线无所谓。出现即卖</div>
                        `
                    },
                    {
                        title: '看跌阴线4（个股，周线）',
                        smallImg: 'gupiao/价格中枢/看跌阴线/logo4.png',
                        desc: '下跌后的筑底',
                        mainImg: 'gupiao/价格中枢/看跌阴线/kdyx4.png',
                        example: ['gupiao/价格中枢/看跌阴线/example4-1.png', 'gupiao/价格中枢/看跌阴线/example4-2.png', 'gupiao/价格中枢/看跌阴线/example4-3.png'],
                        remark: `
                            <div>止盈： 50%+ </div>
                            <div>止损： 近期最低价 </div>
                            <div>光头不光脚(可以有一点点上影线，最好没有)</div>
                            <div>第二周 只能阳线</div>
                            <div>周中买入（即确定后，周三、周四买入）</div>
                        `
                    },
                    {
                        title: '上涨诱空大阴线抄底（个股，日线）',
                        smallImg: 'gupiao/诱空抄底/logo.png',
                        desc: '上涨途中的追涨抢跑',
                        mainImg: 'gupiao/诱空抄底/szjgcddwykdyx.png',
                        example: ['gupiao/诱空抄底/example.png', 'gupiao/诱空抄底/example2.png', 'gupiao/诱空抄底/example3.png', 'gupiao/诱空抄底/example4.png'],
                        remark: `
                            <div>大阴线吃掉的涨幅，可以是阳线也可以有阴线</div>
                            <div>不是低位也可以，只要在上涨趋势中即可</div>
                            <div style="color:#ff891b">主力操盘，成交量可以做假。但是只能放量做假</div>
                        `
                    },
                    {
                        title: '否极泰来',
                        smallImg: 'gupiao/否极泰来/logo.png',
                        desc: '真正的底部模型',
                        mainImg: 'gupiao/否极泰来/pjtl.png',
                        example: ['gupiao/否极泰来/example1.png', 'gupiao/否极泰来/example2.png'],
                        remark: `
                            <div>A、C 也可以是阳线，只要 C 比 A 低</div>
                            <div>B也可以是波动很大的横盘</div>
                            <div>D只要是阳线，也可以是十字星</div>
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
                        example: ['gupiao/神龙摆尾1/example1.png', 'gupiao/神龙摆尾1/example2.png', 'gupiao/神龙摆尾1/example2.png'],
                        remark: `
                            <div>盈利30% - 50%</div>
                            <div>下影线可以扎破箱体，但实体一定不能</div>
                            <div>V字型横盘也可以，但是不好</div>
                            <div>止盈的50%是从第一个涨停板的收盘价开始算，而不是买入的开盘价</div>
                        `
                    },
                    {
                        title: '神龙摆尾2（个股，日线）',
                        smallImg: 'gupiao/神龙摆尾2/logo.png',
                        desc: '筑底后震荡的第一个涨停板',
                        mainImg: 'gupiao/神龙摆尾2/slbw2.png',
                        example: ['gupiao/神龙摆尾2/example1.png', 'gupiao/神龙摆尾2/example2.png', 'gupiao/神龙摆尾2/example2.png'],
                        remark: `
                            <div>盈利30% - 50%</div>
                            <div>k线的收盘价不能跌破涨停板的收盘价</div>
                            <div>下影线可以刺穿</div>
                            <div>如果是阴线，则任意位置(实体、影线)都不能跌破箱体</div>
                            <div>成交量依次降低也可以，最好还是5和10的死叉</div>
                        `
                    },
                    {
                        title: '神龙摆尾3（个股，日线）',
                        smallImg: 'gupiao/神龙摆尾3/logo.png',
                        desc: '筑底后震荡的第一个涨停板',
                        mainImg: 'gupiao/神龙摆尾3/slbw.png',
                        example: ['gupiao/神龙摆尾3/example1.png', 'gupiao/神龙摆尾3/example2.png', 'gupiao/神龙摆尾3/example3.png'],
                        remark: `
                            <div>振幅差不多5%即可</div>
                            <div>最好出现在上涨初期</div>
                            <div>卖点自己把握</div>
                            <div>和神1区别就是不需要一个长周期的横盘后的涨停板</div>
                        `
                    },
                    {
                        title: '神龙摆尾4（个股，日线）',
                        smallImg: 'gupiao/神龙摆尾4/logo.png',
                        desc: '（21/07/24 - 2:18）',
                        mainImg: 'gupiao/神龙摆尾4/slbw4.png',
                        example: ['gupiao/神龙摆尾4/example1.png', 'gupiao/神龙摆尾4/example2.png'],
                        remark: ``
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
                            <div>是在上涨结构中，而不是在上涨趋势中</div>
                        `
                    },
                    {
                        title: '以逸待劳（个股，日线）',
                        smallImg: 'gupiao/以逸待劳/logo.png',
                        desc: '底部的主力洗盘',
                        mainImg: 'gupiao/以逸待劳/yydl.png',
                        example: ['gupiao/以逸待劳/example1.png', 'gupiao/以逸待劳/example2.png', 'gupiao/以逸待劳/example3.png'],
                        remark: `
                            <div>一定是下跌之后的上涨中</div>
                            <div>第五日的只要是阳线就行。不管高开低开、放量缩量、真假都无所谓</div>
                            <div>等待一个爆发，没有可继续等待</div>
                        `
                    },
                    {
                        title: '出水芙蓉（个股，日线）',
                        smallImg: 'gupiao/出水芙蓉/logo.png',
                        desc: '主力低位洗盘模型，大盘比较弱的时候用',
                        mainImg: 'gupiao/出水芙蓉/csfr.png',
                        example: ['gupiao/出水芙蓉/example1.png', 'gupiao/出水芙蓉/example2.png', 'gupiao/出水芙蓉/example3.png'],
                        remark: `
                            <div>最好不要十字星</div>
                        `
                    },
                    {
                        title: '一箭双雕（个股，日线）',
                        smallImg: 'gupiao/一箭双雕/logo.png',
                        desc: '中继加速模型，主力拉升前的洗盘',
                        mainImg: 'gupiao/一箭双雕/yjsd.png',
                        example: ['gupiao/一箭双雕/example1.png', 'gupiao/一箭双雕/example2.png', 'gupiao/一箭双雕/example3.png', 'gupiao/一箭双雕/example4.png', 'gupiao/一箭双雕/example5.png'],
                        remark: `
                            <div>缓慢上涨 到 急速拉升 的过渡点</div>
                            <div>机会较少，盈利也会很多的。止盈自己把握，也可以使用推高止损的方式扩大盈利</div>
                            <div>两个阴线最好是高开的(加分项，不是必需的)</div>
                            <div>案例中的第一根阳线，可以不是很大</div>
                        `
                    },
                    {
                        title: '柳暗花明（个股，日线）',
                        smallImg: 'gupiao/柳暗花明/logo.png',
                        desc: '底部反转模型，主力底部的强势洗盘',
                        mainImg: 'gupiao/柳暗花明/lahm.png',
                        // example: ['gupiao/柳暗花明/example1.png', 'gupiao/柳暗花明/example2.png', 'gupiao/柳暗花明/example3.png'],
                        remark: `
                            <div>出现以后，必然是底</div>
                        `
                    },
                    {
                        title: '葛式八法 - 买2（个股，周日线）',
                        smallImg: 'gupiao/葛式八法/logo2.png',
                        
                        mainImg: 'gupiao/葛式八法/买2.png',
                        example: ['gupiao/葛式八法/example2-1.png', 'gupiao/葛式八法/example2-2.png'],
                        remark: `
                            <div></div>
                        `
                    },
                    {
                        title: '神奇均线（个股，日线）',
                        smallImg: 'gupiao/神奇均线/logo.png',
                        desc: '下跌横盘后， 上涨初期',
                        conditions: ['回调的幅度(举例跳起来之前的下蹲，不能太低不能太高)', '有效突破/有效支撑(举例箱体的上下沿)'],
                        mainImg: 'gupiao/神奇均线/sqjx.png',
                        example: ['gupiao/神奇均线/example1.png', 'gupiao/神奇均线/example2.png'],
                        remark: `
                            <div><span style="color: #F4882F">快：5；</span><span style="color: #0096EF">中：13；</span><span style="color: #000">慢：34</span></div>
                            <div style="font-size: 20px">A：</div>
                            <div>k线允许跌破慢速均线</div>
                            <div style="font-size: 20px">B：</div>
                            <div>慢速均线、中速均线下穿快速均线后，无论谁上谁下</div>
                        `
                        
                    },
                    {
                        title: '神奇数字（个股，月>周>日）',
                        smallImg: 'gupiao/神奇数字/logo.png',
                        desc: '（21/07/31 - 2:20）',
                        mainImg: 'gupiao/神奇数字/sqsz.png',
                        example: ['gupiao/神奇数字/example1.png', 'gupiao/神奇数字/example2.png'],
                        remark: `
                            <div>买入后短期内即可达到目标</div>
                        `
                        
                    },
                    {
                        title: '鱼跃龙门（个股，月线）',
                        smallImg: 'gupiao/鱼跃龙门/logo.png',
                        // desc: '',
                        mainImg: 'gupiao/鱼跃龙门/yylm.png',
                        example: ['gupiao/鱼跃龙门/example1.png', 'gupiao/鱼跃龙门/example2.png'],
                        remark: `
                            <div>时间不确定，有可能3月，有可能半年以上</div>
                            <div>不设止损</div>
                            <div>从下跌到翻倍, 4年以上</div>
                            <div>筑底时间要长</div>
                            <div>底部可是,单底\多底\圆弧底,</div>
                        `
                        
                    },
                    {
                        title: '隔山打牛（个股，日线）',
                        smallImg: 'gupiao/隔山打牛/logo.png',
                        desc: '上涨初期或中期',
                        mainImg: 'gupiao/隔山打牛/gsdn.png',
                        example: ['gupiao/隔山打牛/example1.png', 'gupiao/隔山打牛/example2.png'],
                        remark: `
                            <div>成交量不必依次降低</div>
                        `
                        
                    },
                    {
                        title: '大有（个股，日线）',
                        smallImg: 'gupiao/大有/logo.png',
                        desc: '上涨初期的洗盘模型（21/07/10 - 2:30）',
                        mainImg: 'gupiao/大有/dy.png',
                        example: ['gupiao/大有/example1.png', 'gupiao/大有/example2.png', 'gupiao/大有/example3.png'],
                        remark: `
                            <div>4连阳就是4个，3个不行，5个也不行</div>
                            <div>4连阳实体应该都不大</div>
                            <div>最后的阳线最好不大，也可以是涨停板</div>
                            <div>期望是买入后才涨，不应该是涨过了才买</div>
                        `
                        
                    },
                    {
                        title: '一触即发(个股， 日线)',
                        smallImg: 'gupiao/窓璧轴/一触即发/logo.png',
                        desc: '窓璧轴理论（21/07/17 - 1:30）',
                        mainImg: 'gupiao/窓璧轴/一触即发/ycjf.png',
                        example: ['gupiao/窓璧轴/一触即发/example1.png', 'gupiao/窓璧轴/一触即发/example2.png', 'gupiao/窓璧轴/一触即发/example3.png'],
                        remark: `
                            <div>运行一周以上，>5天才有效</div>
                            <div>上涨/下跌，应该能创新高/新低</div>
                            <div>连续的涨停板没有参考价值</div>
                        `
                        
                    },
                    {
                        title: '一举中第(个股， 日线)',
                        smallImg: 'gupiao/窓璧轴/一举中第/logo.png',
                        desc: '窓璧轴理论',
                        mainImg: 'gupiao/窓璧轴/一举中第/yjzd.png',
                        example: ['gupiao/窓璧轴/一举中第/example1.png', 'gupiao/窓璧轴/一举中第/example2.png', 'gupiao/窓璧轴/一举中第/example3.png'],
                        remark: `
                            <div>运行一周以上，最好>5天</div>
                            <div>影线填补、实体填补都可以</div>
                            <div>第二次填补要小于之前缺口的1/2，也就是小部分</div>
                        `
                        
                    },
                    {
                        title: '一线生机(个股， 日线)',
                        smallImg: 'gupiao/窓璧轴/一线生机/logo.png',
                        desc: '窓璧轴理论',
                        mainImg: 'gupiao/窓璧轴/一线生机/yxsj.png',
                        example: ['gupiao/窓璧轴/一线生机/example1.png', 'gupiao/窓璧轴/一线生机/example2.png'],
                        remark: `
                            <div>等待确定的阳线： 中阳线、大阳线</div>
                        `
                        
                    },
                    {
                        title: '一反常态(个股， 日线)',
                        smallImg: 'gupiao/窓璧轴/一反常态/logo.png',
                        desc: '窓璧轴理论',
                        mainImg: 'gupiao/窓璧轴/一反常态/yfct.png',
                        example: ['gupiao/窓璧轴/一反常态/example1.png', 'gupiao/窓璧轴/一反常态/example2.png', 'gupiao/窓璧轴/一反常态/example3.png'],
                        remark: `
                            <div>实体完全填补，无论阴线、阳线</div>
                            <div></div>
                            <div>说明主力控盘力度极强</div>
                        `
                        
                    },
                    {
                        title: '蜻蜓点水(个股， 日线)',
                        smallImg: 'gupiao/蜻蜓点水/logo.png',
                        desc: '价格筑底 上涨初期 (缺口理论应用)',
                        mainImg: 'gupiao/蜻蜓点水/qtds.png',
                        example: ['gupiao/蜻蜓点水/example1.png', 'gupiao/蜻蜓点水/example2.png', 'gupiao/蜻蜓点水/example3.png'],
                        remark: `
                            <div>缺口被填补无论阴阳线或影线</div>
                        `
                    },
                    {
                        title: '结界均线(个股， 日线)',
                        smallImg: 'gupiao/结界均线/logo.png',
                        desc: '75日 均线（21/07/17 - 2:53）',
                        mainImg: 'gupiao/结界均线/jx.png',
                        example: ['gupiao/结界均线/example1.png', 'gupiao/结界均线/example2.png', 'gupiao/结界均线/example3.png'],
                        remark: `
                            <div>实体不能跌破均线</div>
                            <div>必须要有下影线（影线可以不破均线）</div>
                        `
                    },
                    {
                        title: '龙战于野(个股， 日线)',
                        smallImg: 'gupiao/龙战于野/logo.png',
                        desc: '低位涨停（21/07/17 - 3:20）',
                        mainImg: 'gupiao/龙战于野/lzyy.png',
                        example: ['gupiao/龙战于野/example1.png', 'gupiao/龙战于野/example2.png', 'gupiao/龙战于野/example3.png'],
                        remark: `
                            <div>涨停板可以是一字</div>
                            <div>大阴线也可以是涨停板</div>
                            <div>阴、阳线高开低开平开无所谓</div>
                            <div>低位、中位都可以，也可以横盘中使用，但必须是低位</div>
                            <div>止损： 涨停版的开盘价（适用于所有用到涨停板的模型）</div>
                        `
                    },
                    {
                        title: 'v型反转(个股， 日线)',
                        smallImg: 'gupiao/v型反转/logo.png',
                        desc: '',
                        mainImg: 'gupiao/v型反转/vxfz.png',
                        example: ['gupiao/v型反转/example1.png', 'gupiao/v型反转/example2.png', 'gupiao/v型反转/example3.png', 'gupiao/v型反转/example4.png'],
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
            }
        }
    }
</script>

<style lang="less" scoped>
.gupiao-collapse {
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