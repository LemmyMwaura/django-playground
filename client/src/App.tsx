import { useEffect, useState } from "react"
import "./App.css"

// axiosInstance
import axiosInstance from "./utils/axios"

interface ServerResponse {
  data: ServerData
}

interface ServerData {
  title: string
  content: string
  price : number
}

function App() {
  const [data, setData] = useState(null)

  useEffect(() => {
    const getData = async () => {
      const { data } = await axiosInstance
        .get<ServerData>("/api")
        .catch((e) => console.log(e))

      setData(data)
    }

    getData()
  }, [])

  return (
    <div className="App">
      <h2>Home</h2>
      <div>
        <h2>DATA</h2>
        <h3>{data?.title}</h3>
        <h3>{data?.content}</h3>
        <h3>{data?.price}</h3>
      </div>
    </div>
  )
}

export default App
