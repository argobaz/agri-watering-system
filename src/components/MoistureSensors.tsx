import { useState, useEffect } from 'react';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { SoilMoistureSensor } from './SoilMoistureSensor';
import { WateringControl } from './WateringControl';
import { calculateMoistureAverage, MOISTURE_THRESHOLDS } from '@/lib/moisture';

interface MoistureSensorsProps {
  isWatering: boolean;
  onToggleWatering: () => void;
}

export function MoistureSensors({ isWatering, onToggleWatering }: MoistureSensorsProps) {
  const [sensors, setSensors] = useState(['', '', '']);
  const [average, setAverage] = useState<number>(0);

  useEffect(() => {
    const values = sensors.map(v => parseFloat(v) || 0);
    const avg = calculateMoistureAverage(values);
    setAverage(avg);
  }, [sensors]);

  const updateSensor = (index: number, value: string) => {
    setSensors(prev => {
      const newSensors = [...prev];
      newSensors[index] = value;
      return newSensors;
    });
  };

  const shouldStartWatering = average < MOISTURE_THRESHOLDS.LOW;
  const shouldStopWatering = average > MOISTURE_THRESHOLDS.HIGH;

  return (
    <div className="space-y-4">
      <div className="grid grid-cols-3 gap-4">
        {sensors.map((value, index) => (
          <SoilMoistureSensor
            key={index}
            id={index + 1}
            value={value}
            onChange={(value) => updateSensor(index, value)}
          />
        ))}
      </div>

      {average > 0 && (
        <Alert className={shouldStartWatering ? 'bg-destructive/20' : shouldStopWatering ? 'bg-green-500/20' : 'bg-muted'}>
          <AlertDescription>
            Average Moisture: {average.toFixed(1)}%
          </AlertDescription>
        </Alert>
      )}

      <div className="flex justify-center gap-4">
        <WateringControl
          isWatering={isWatering}
          onToggle={onToggleWatering}
          autoMode={shouldStartWatering || shouldStopWatering}
          autoAction={shouldStartWatering ? 'start' : shouldStopWatering ? 'stop' : null}
        />
      </div>
    </div>
  );
}