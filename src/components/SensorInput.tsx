import { Input } from '@/components/ui/input';
import { LucideIcon } from 'lucide-react';

interface SensorInputProps {
  label: string;
  value: string;
  onChange: (value: string) => void;
  placeholder: string;
  Icon: LucideIcon;
  unit: string;
}

export function SensorInput({ label, value, onChange, placeholder, Icon, unit }: SensorInputProps) {
  return (
    <div className="space-y-2">
      <label className="flex items-center gap-2 text-sm font-medium">
        <Icon className="w-4 h-4" />
        {label} ({unit})
      </label>
      <Input
        type="number"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        className="bg-background"
      />
    </div>
  );
}