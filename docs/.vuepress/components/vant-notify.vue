<template>
  <div></div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      default: ''
    }
  },
  mounted() {
    this.$notify({
      type: 'primary',
      message: this.message,
      duration: 5000
    });
  }
};
</script>

<style lang="less" scoped>
</style>