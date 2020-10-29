<template>
  <div :title="name + ' ' + lastName + ' ,id: ' + id">
    <span>{{name.substring(0,1)}}{{lastName.substring(0,1)}}</span>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class UserBubble extends Vue{
  @Prop() id!: string
  @Prop() name!: string
  @Prop() lastName!: string
}


</script>

<style scoped>

</style>