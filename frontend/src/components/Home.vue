<template>
 <div class="Home">
   <template v-if="this.user">
      <div class="row">
      <div class="col-sm-6 spotify-column-res">
        <div class="res-content">
      <h1>Hi there, {{ this.user.display_name }}</h1>
      <!--img :src="this.user.images[0].url" alt="profile_picture" class="profile_pic"-->
      <p>
        <a :href="this.user.external_urls.spotify">Link to your profile</a>
      </p>
      <p>Number of followers: {{ this.user.followers.total }}</p>
      <p>
        <button v-on:click="logOut()" class="btn btn-primary btn-dark">Log out</button>
      </p>
        </div>
      </div>
      <div class="col-sm-6 youtube-column">
        <svg class="youtube-icon" xmlns="http://www.w3.org/2000/svg" width="20%" height="20%" viewBox="0 0 24 24"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/></svg>
      </div>
      </div>
    </template>
    <template v-else>
      <div class="row">
        <div class="col-sm-6 spotify-column">
          <a href="https://rx00516zgh.execute-api.us-west-2.amazonaws.com/dev/spotify/">
            <svg class="spotify-icon" enable-background="new 0 0 24 24" height="20%" viewBox="0 0 24 24" width="20%" xmlns="http://www.w3.org/2000/svg"><circle class="spotify-icon-bg" cx="12" cy="12" fill="#4caf50" r="12"/><g class="spotify-icon-fill" fill="#212121"><path d="m16.872 17.656v.001c-.203 0-.329-.063-.518-.174-3.019-1.82-6.532-1.896-10.002-1.185-.189.049-.436.126-.576.126-.47 0-.765-.373-.765-.765 0-.499.295-.736.659-.813 3.963-.875 8.013-.798 11.467 1.268.295.189.47.358.47.798 0 .438-.344.744-.735.744z"/><path d="m18.175 14.483h-.001c-.252 0-.421-.111-.596-.203-3.025-1.79-7.533-2.512-11.545-1.423-.232.063-.358.126-.576.126-.518 0-.938-.421-.938-.938s.252-.861.75-1.001c1.345-.378 2.719-.659 4.732-.659 3.14 0 6.174.779 8.565 2.202.392.232.547.533.547.953-.005.521-.411.943-.938.943z"/><path d="m4.548 6.998c1.703-.499 3.61-.735 5.686-.735 3.532 0 7.234.735 9.939 2.313.378.218.624.518.624 1.093 0 .658-.533 1.127-1.122 1.127l-.001-.001c-.252 0-.407-.063-.625-.189-3.444-2.056-9.605-2.549-13.591-1.436-.175.048-.393.125-.625.125-.639 0-1.127-.499-1.127-1.142 0-.657.407-1.029.842-1.155z"/></g></svg>
          </a>
        </div>
        <div class="col-sm-6 youtube-column">
          <svg class="youtube-icon" xmlns="http://www.w3.org/2000/svg" width="20%" height="20%" viewBox="0 0 24 24"><path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"/></svg>
        </div>
      </div>
    </template>
</div>
</template>

<script>
import Vue from 'vue'
export default {
  name: 'Home',
  computed: {
        user() {
                return this.$store.getters.getUser
            }
        },
        methods: {
            logOut() {
                this.$store.commit('mutateUser', null);
                this.$router.push({ name: 'Home'})
            }
        },
        created() {
            if (this.$route.query) {
                console.log(this.$route.query)
                Vue.axios.get('https://api.spotify.com/v1/me', {
                    headers: {
                        'Authorization': 'Bearer ' + this.$route.query.access_token
                    }
                }).then((response) => {
                    this.$store.commit('mutateUser', response.data);
                    console.log('Response from server: ');
                    console.log(this.$store.state.user);
                })
            }
        }
}

</script>

<style scoped>
.row{
  height: 100vh;
}
.spotify-column {
    background: #000000;
    align-items: center;
    text-align: center;
}
.spotify-column:hover {
    background: #1fb954;
}

.spotify-column-res {
    background: #1fb954;
    align-items: center;
    text-align: center;
}

.res-content {
  position: absolute;
  top: 40%;
  left: 35%;
}

.spotify-icon {
  position: absolute;
  top: 40%;
  left: 40%;
}

 .spotify-column:hover .spotify-icon .spotify-icon-bg {
    fill: #000000;
}

.spotify-column:hover .spotify-icon .spotify-icon-fill {
    fill: #ffffff;
}

.youtube-column {
  background: #ffffff;
  align-items: center;
}

.youtube-column:hover {
    background: #ed3742;
}

.youtube-icon {
  position: absolute;
  top: 40%;
  left: 40%;
  fill: #ed3742;
}

.youtube-column:hover .youtube-icon {
  fill: #ffffff;
}

.youtube-column:hover .spotify-column {
  background: #ffffff;
}


</style>
