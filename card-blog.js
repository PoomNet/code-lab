Vue.component('card-blog', {
    template:
        `
        <div class="card my-3">
        <img src="https://pbs.twimg.com/profile_images/875996174305472512/upM71pVR_400x400.jpg" alt="..." class="card-img-top img-fluid"> 
        <div class="card-body">
        <h5 class="card-title">{{blog.title}}<span class="badge badge-success ml-5">Likes: {{blog.likes}}</span></h5>
         <p class="card-text">
    {{blog.content}}
    <br> 
    <small class="text-muted">Create By: </small> 
    <small class="text-muted ml-5">Create Date: </small>
    </p> 
    <button class="btn btn-success" @click="$emit('add-like')">
    I like this!
    </button>
    <button class="btn btn-info">
    Show comment...
    </button>
    <button class="btn btn-info">
    New comment
    </button>
    <div class="card mt-2 text-dark" v-for="comment in blog.comments">
    <div class="card-body">
    <h6 class="card-title">{{comment.text}}</h6> 
    <p class="card-text">
          Curious which components explicitly require jQuery, our JS, and Popper.js? Click the show components link below.<br> <small class="text-muted">Create By: </small> <small class="text-muted ml-5">Create Date: </small></p>
          </div>
          </div>
          </div>
          </div>
          `
    ,
    props:['blog'],
        data: {
          searchText:'',
          blogs: [
            {
              id: 1,
              title: "Hello World!",
              content: "I love Vue.js. It is so cool and easy!",
              createBy: "Bundit",
              createDate: new Date().toLocaleString(),
              image:
                "https://pbs.twimg.com/profile_images/875996174305472512/upM71pVR_400x400.jpg",
              fb: "https://vuejs.org",
              likes: 0,
              comments: [
                { text: "Yes I agree!", likes: 0, createBy: "Jack" },
                { text: "Could not agree more!", likes: 0, createBy: "John" }
              ]
            },
            {
              id: 2,
              title: "Hello 12345!",
              content:
                "An sincerity so extremity he additions. Her yet there truth merit. Mrs all projecting favourable now unpleasing. Son law garden chatty temper. Oh children provided to mr elegance marriage strongly. Off can admiration prosperous now devonshire diminution law.",
              createBy: "Job",
              createDate: new Date().toLocaleString(),
              image:
                "https://pbs.twimg.com/profile_images/875996174305472512/upM71pVR_400x400.jpg",
              fb: "https://vuejs.org",
              likes: 0,
              comments: [
                {
                  text: "He oppose at thrown desire of no.",
                  likes: 0,
                  createBy: "Jack"
                },
                { text: "Noooooo!", likes: 0, createBy: "John" },
                {
                  text:
                    "Announcing impression unaffected day his are unreserved indulgence.",
                  likes: 0,
                  createBy: "John"
                }
              ]
            },
            {
              id: 3,
              title: "Hello World!",
              content: "I love Vue.js. It is so cool and easy!",
              createBy: "Bundit",
              createDate: new Date().toLocaleString(),
              image:
                "https://pbs.twimg.com/profile_images/875996174305472512/upM71pVR_400x400.jpg",
              fb: "https://vuejs.org",
              likes: 0,
              comments: [{ text: "Yes I agree!", likes: 0, createBy: "Jack" }]
            },
            {
              id: 4,
              title: "Bah bah bah...",
              content:
                "Folly words widow one downs few age every seven. If miss part by fact he park just shew.",
              createBy: "Job",
              createDate: new Date().toLocaleString(),
              image:
                "https://pbs.twimg.com/profile_images/875996174305472512/upM71pVR_400x400.jpg",
              fb: "https://vuejs.org",
              likes: 0,
              comments: [
                { text: "Yes I agree!", likes: 0, createBy: "Jack" },
                { text: "Could not agree more!", likes: 0, createBy: "John" },
                { text: "Yes I agree!", likes: 0, createBy: "Job" },
                { text: "Could not agree more!", likes: 0, createBy: "John" }
              ]
            },
            {
              id: 5,
              title: "Hey hey hey!",
              content:
                "Was certainty remaining engrossed applauded sir how discovery. Settled opinion how enjoyed greater joy adapted too shy. Now properly surprise expenses interest nor replying she she.",
              createBy: "Bundit",
              createDate: new Date().toLocaleString(),
              image:
                "https://pbs.twimg.com/profile_images/875996174305472512/upM71pVR_400x400.jpg",
              fb: "https://vuejs.org",
              likes: 10,
              comments: [
                { text: "Yes I agree!", likes: 0, createBy: "Jack" },
                { text: "Could not agree more!", likes: 0, createBy: "John" }
              ]
            }
          ],
          selects: [],
          tooManyPost: false
        },
        methods:{
          changeBGColor(){
            console.log('change bg color')
          },
          showComment(){
            console.log('show comment')
          }
        },
        computed:{
          blogSearchResult(){
            return this.blogs.filter(blog => {
              let searchtext = this.searchText.toLowerCase()

              let isintitle = blog.title.toLowerCase().includes(searchtext)
              let isincontent = blog.content.toLowerCase().includes(searchtext)
              return isincontent | isintitle
            })
          }
        },
        watch:{

        }
})