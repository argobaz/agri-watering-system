import { useState } from 'react';
import { Card } from '@/components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { ThermometerSun, Droplets, Beaker } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';
import { SensorInput } from '@/components/SensorInput';
import { CameraView } from '@/components/CameraView';
import { MoistureSensors } from '@/components/MoistureSensors';

function App() {
  const [temperature, setTemperature] = useState('');
  const [humidity, setHumidity] = useState('');
  const [soilPH, setSoilPH] = useState('');
  const [isWatering, setIsWatering] = useState(false);
  const [selectedCamera, setSelectedCamera] = useState('');
  const { toast } = useToast();

  const toggleWatering = () => {
    setIsWatering(!isWatering);
    toast({
      title: isWatering ? "Watering Stopped" : "Watering Started",
      description: isWatering ? "The watering system has been stopped" : "The watering system has been activated"
    });
  };

  const selectCamera = (camera: string) => {
    setSelectedCamera(camera);
    toast({
      title: "Camera Selected",
      description: `Switched to ${camera}`
    });
  };

  return (
    <div className="min-h-screen bg-background p-8">
      <Card className="max-w-4xl mx-auto p-6 bg-card">
        <h1 className="text-3xl font-bold text-center mb-8 text-primary">Field Monitoring Dashboard</h1>
        
        <Tabs defaultValue="sensors" className="w-full">
          <TabsList className="grid w-full grid-cols-2 mb-8">
            <TabsTrigger value="sensors">Sensor Data</TabsTrigger>
            <TabsTrigger value="cameras">Cameras</TabsTrigger>
          </TabsList>

          <TabsContent value="sensors">
            <div className="grid gap-6">
              <SensorInput
                label="Temperature"
                value={temperature}
                onChange={setTemperature}
                placeholder="Enter temperature"
                Icon={ThermometerSun}
                unit="°C"
              />

              <SensorInput
                label="Humidity"
                value={humidity}
                onChange={setHumidity}
                placeholder="Enter humidity"
                Icon={Droplets}
                unit="%"
              />

              <SensorInput
                label="Soil pH"
                value={soilPH}
                onChange={setSoilPH}
                placeholder="Enter soil pH"
                Icon={Beaker}
                unit="pH"
              />

              <MoistureSensors
                isWatering={isWatering}
                onToggleWatering={toggleWatering}
              />
            </div>
          </TabsContent>

          <TabsContent value="cameras">
            <CameraView
              selectedCamera={selectedCamera}
              onSelectCamera={selectCamera}
            />
          </TabsContent>
        </Tabs>
      </Card>
    </div>
  );
}

export default App;