import { Sprout } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

interface SoilMoistureInputProps {
  value: string;
  onChange: (value: string) => void;
  onCalculate: () => void;
}

export function SoilMoistureInput({ value, onChange, onCalculate }: SoilMoistureInputProps) {
  return (
    <div className="space-y-2">
      <label className="flex items-center gap-2 text-sm font-medium">
        <Sprout className="w-4 h-4" />
        Soil Moisture Values (%)
      </label>
      <div className="flex gap-2">
        <Input
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="Enter values separated by commas (e.g., 10,20,30)"
          className="bg-background"
        />
        <Button onClick={onCalculate} variant="secondary">
          Calculate
        </Button>
      </div>
    </div>
  );
}