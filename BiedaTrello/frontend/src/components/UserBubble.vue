<template>

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
  @Prop() private user!: User
}


</script>

<style scoped>

</style>