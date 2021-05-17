import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import React, {useEffect, useState} from 'react';

function MainPage() {

  const [quotes, setQuotes] = useState([])

  useEffect(() => {
    axios({
      method: "GET",
      url: "http://127.0.0.1:8010/api/v1/quotes/",
    }).then(response => {
      setQuotes(response.data)
    });

  }, [])


  return (<>
      <div className='block'>
        {quotes.map(q => (
          <div key={q.id} className="card bg-dark text-white"
               style={{border: '4px solid black', marginTop: 0, position: 'relative'}}>
            <img className="card-img" src={q.image} alt="Card image"/>
            <div className="card-img-overlay" style={{MarginBottom: 1,}}>

              <p className="font-italic font-weight-bold"
                 style={{position: 'absolute', bottom: 20, textAlign: 'left',}}>„{q.text}“</p>
              <p className="font-italic"
                 style={{position: 'absolute', bottom: 0, textAlign: 'left', marginBottom: 10}}>{q.author}</p>
            </div>
          </div>))}

      </div>
    </>
  )
}


export default MainPage;
