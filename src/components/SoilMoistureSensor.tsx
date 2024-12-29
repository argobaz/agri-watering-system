import { Input } from '@/components/ui/input';
import { Card } from '@/components/ui/card';
import { Droplets } from 'lucide-react';

interface SoilMoistureSensorProps {
  id: number;
  value: string;
  onChange: (value: string) => void;
}

export function SoilMoistureSensor({ id, value, onChange }: SoilMoistureSensorProps) {
  return (
    <Card className="p-4">
      <label className="flex items-center gap-2 text-sm font-medium mb-2">
        <Droplets className="w-4 h-4" />
        Sensor {id}
      </label>
      <Input
        type="number"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Enter moisture %"
        min="0"
        max="100"
        className="bg-background"
      />
    </Card>
  );
}