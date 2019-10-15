<template>
  <div></div>
</template>

<script>
export default {
  mounted() {
    this.$notify({
      type: 'primary',
      message: "新增 获取list中任意属性值， 详见第五条",
      duration: 5000
    });
  }
};
</script>

<style lang="less" scoped>
</style>