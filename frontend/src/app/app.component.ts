import { Component, OnDestroy, OnInit } from '@angular/core';
import { interval } from 'rxjs/internal/observable/interval';
import { Subject } from 'rxjs/internal/Subject';
import { takeUntil } from 'rxjs/operators';
import { SensorDataService } from './services/sensor-data.service';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit, OnDestroy {
    temperature: number = 0.0;
    pressure: number = 0.0;
    humidity: number = 0.0;
    gas_resistance: number = 0.0;
    air_quality: number = 0.0;
    fire_detected: boolean = false;

    private destroyView$ = new Subject();

    constructor(private sensorDataService: SensorDataService) {}

    getSensorData(): void {
        this.sensorDataService.getSensorData().subscribe((sensorData) => {
            this.temperature = sensorData.temperature;
            this.pressure = sensorData.pressure;
            this.humidity = sensorData.humidity;
            this.gas_resistance = sensorData.gas_resistance;
            this.air_quality = sensorData.air_quality;
            this.fire_detected = sensorData.fire_detected
        });
    }

    public getColor(fire_detected: boolean): string{
        return fire_detected ? "red" : "green";
    }

    ngOnInit(): void {
        interval(3000)
            .pipe(takeUntil(this.destroyView$))
            .subscribe(() => this.getSensorData());
    }

    ngOnDestroy(): void {
        this.destroyView$.next(true);
        this.destroyView$.complete();
    }
}
