<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div v-for="user_ql in users">
      <UserBubble :name="user_ql.name" :id="user_ql.id" :lastName="user_ql.lastName"> </UserBubble>
    </div>
  </div>

</template>
<script lang="ts">
import gql from 'graphql-tag'
import UserBubble from "@/components/UserBubble.vue";

const UsersQuery = gql`
    query {
        users{
            id
            name
            lastName
        }
    }
`;

export default {
  components: {UserBubble},
  data(){
    return {
      users: '',
    }
  },

  apollo: {
    users: UsersQuery
  }
}
</script>