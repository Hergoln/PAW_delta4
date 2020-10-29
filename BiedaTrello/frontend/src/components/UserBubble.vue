<template>
  <div title="{{user.name}} {{user.last_name}}, id: {{user.id}}">
    <span>{{user.name.substring(0,1)}}{{user.last_name.substring(0,1)}}</span>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

export type User = {
    id: number
    name: string
    last_name: string
}

@Component
export default class UserBubble extends Vue{
  @Prop() user!: User
}


</script>

<style scoped>

</style>