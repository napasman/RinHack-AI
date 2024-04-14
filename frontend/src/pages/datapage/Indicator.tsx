import { useEffect, useState } from "react"
import custom from "./Indicator.module.css"
import Pagination from '@mui/material/Pagination'
import axios from "axios"

type dataArr = {
    traffic: dataF[]
}

type dataF = {
    id: number,
    time_stamp: string,
    source_ip: string,
    destination_ip: string,
    protocol: string,
    port: string,
    packet_size: string,
    prediction: string,
}

function Indicator() {

    const [page, setPage] = useState(1)
    const [data, setData] = useState<dataArr>([])
    useEffect(() => {
        async function fetchData() {
            try {
                const res = await axios.get("http://localhost:3000/traffic")
                    .then(res => res.data)
                    .then(res => setData(res))
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }
        fetchData()

        const interval = setInterval(fetchData, 1000);

        return () => clearInterval(interval);
    }, [])

    function handleChangePage(e, p: number) {
        setPage(p)
    }

    console.log(data)

    return (
        <div className={custom.main}>
            <div className={custom.title}>
                <h1>Отслеживание вашего трафика </h1>
                <Pagination onChange={handleChangePage} page={page} count={data.traffic?.length} variant="outlined" color="primary" />
            </div>

            <ul>
                {
                    data?.traffic
                        ?.filter(item => item.id === page)
                        .map(res => (
                            <>
                                <li>
                                    <p>time_stamp: {res?.time_stamp}</p>
                                </li>
                                <li><p>source_ip: {res?.source_ip}</p></li>
                                <li><p>destination_ip: {res?.destination_ip}</p></li>
                                <li><p>protocol: {res?.protocol}</p></li>
                                <li><p>port: {res?.port}</p></li>
                                <li><p>packet_size: {res?.packet_size}</p></li>
                                <li><p>prediction: {res?.prediction}</p></li>
                            </>
                        ))
                }
            </ul>
        </div>
    )
}

export default Indicator