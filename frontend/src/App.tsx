import './App.css'
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import 'swiper/css/effect-cube';
import 'swiper/css/pagination';

// import required modules
import { EffectCube, Mousewheel, Pagination } from 'swiper/modules';
import Main from './pages/main/Main';
import Indicator from './pages/datapage/Indicator';
function App() {

  const pagination = {
    clickable: true,
  };

  return (
    <div className='app'>
      <Swiper
        loop={false}
        effect={'cube'}
        grabCursor={true}
        cubeEffect={{
          shadow: true,
          slideShadows: true,
          shadowOffset: 20,
          shadowScale: 0.94,
        }}
        mousewheel={true}
        pagination={pagination}
        modules={[EffectCube, Mousewheel, Pagination]}
        className="mySwiper"

      >
        <SwiperSlide>
          <Main />
        </SwiperSlide>
        <SwiperSlide>
          <Indicator />
        </SwiperSlide>
      </Swiper>
    </div>
  )
}

export default App
