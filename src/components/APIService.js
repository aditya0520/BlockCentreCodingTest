export default class APIService{
    // Insert an article
    static InsertArticle(body){
        return fetch(`http://localhost:8000/add_todo`,{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify(body)
        })
    }
}