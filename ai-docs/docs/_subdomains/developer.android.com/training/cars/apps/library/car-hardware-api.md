---
url: https://developer.android.com/training/cars/apps/library/car-hardware-api/
title: Car Hardware APIs \u00a0|\u00a0 Android for Cars \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:46:08.572328+00:00
---

# Car Hardware APIs  |  Android for Cars  |  Android Developers

> Source: https://developer.android.com/training/cars/apps/library/car-hardware-api/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Devices ](https://developer.android.com/develop/devices)
  * [ Android for Cars ](https://developer.android.com/training/cars)



#  Car Hardware APIs Stay organized with collections  Save and categorize content based on your preferences. 

Starting with Car App API level 3, you can use Car App Library APIs to access vehicle properties and sensors.

## Requirements

To use the APIs with Android Auto, start by adding a dependency on `androidx.car.app:app-projected` to the `build.gradle` file for your Android Auto module. For Android Automotive OS, add a dependency on `androidx.car.app:app-automotive` to the `build.gradle` file for your Android Automotive OS module.

Additionally, in your `AndroidManifest.xml` file, you must [declare the relevant permissions](https://developer.android.com/training/permissions/declaring) to request the car data you want to use. The user must also [grant](https://developer.android.com/training/permissions/requesting) these permissions to you. You can use the [same code](https://developer.android.com/training/cars/apps/library/request-permissions) on Android Auto and Android Automotive OS, rather than creating platform-dependent flows. However, the required permissions differ.

## CarInfo

This table describes the properties provided in the [`CarInfo`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo) APIs and the permissions you must request to use them.

Methods | Properties | Permissions:  
Android Auto | Permissions:  
AAOS | Car App API  
---|---|---|---|---  
[`fetchModel`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#fetchModel\(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.Model>\)) | Make, model, year |  | `android.car.permission.CAR_INFO` | 3  
[`fetchEnergyProfile`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#fetchEnergyProfile\(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.EnergyProfile>\)) | EV connector types, fuel types | `com.google.android.gms.permission.CAR_FUEL` | `android.car.permission.CAR_INFO` | 3  
[ `fetchExteriorDimensions` ](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#fetchExteriorDimensions\(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.ExteriorDimensions>\)) _Data available only on some AAOS vehicles that run API 30 or higher._ | Exterior dimensions | N/A | `android.car.permission.CAR_INFO` | 7  
[`addTollListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#addTollListener\(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.TollCard>\)) [`removeTollListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#removeTollListener\(androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.TollCard>\)) | Toll card state, toll card type |  |  | 3  
[`addEnergyLevelListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#addEnergyLevelListener\(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.EnergyLevel>\)) [`removeEnergyLevelListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#removeEnergyLevelListener\(androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.EnergyLevel>\)) | Battery level, fuel level, fuel level low, range remaining | `com.google.android.gms.permission.CAR_FUEL` |  `android.car.permission.CAR_ENERGY`  
  
`android.car.permission.CAR_ENERGY_PORTS`  
  
`android.car.permission.READ_CAR_DISPLAY_UNITS` | 3  
[`addSpeedListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#addSpeedListener\(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.Speed>\)) [`removeSpeedListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#removeSpeedListener\(androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.Speed>\)) | Raw speed, display speed (shown on car's cluster display) | `com.google.android.gms.permission.CAR_SPEED` |  `android.car.permission.CAR_SPEED`  
  
`android.car.permission.READ_CAR_DISPLAY_UNITS` | 3  
[`addMileageListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#addMileageListener\(java.util.concurrent.Executor,%20androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.Mileage>\)) [`removeMileageListener`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo#removeMileageListener\(androidx.car.app.hardware.common.OnCarDataAvailableListener<androidx.car.app.hardware.info.Mileage>\)) | Odometer distance | `com.google.android.gms.permission.CAR_MILEAGE` | _Data not available to Android Automotive OS apps installed from Google Play._ | 3  
  
For example, to get the remaining range, instantiate a `CarInfo` object, then create and register an `OnCarDataAvailableListener`:
    
    
    val carInfo = carContext.getCarService(CarHardwareManager::class.java).carInfo
    
    val listener = OnCarDataAvailableListener<EnergyLevel> { data ->
        if (data.rangeRemainingMeters.status == CarValue.STATUS_SUCCESS) {
            val rangeRemaining = data.rangeRemainingMeters.value
        } else {
            // Handle error
        }
    }
    
    carInfo.addEnergyLevelListener(carContext.mainExecutor, listener)
    // ...
    // Unregister the listener when you no longer need updates
    carInfo.removeEnergyLevelListener(listener)
    
    [CarHardware.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/CarHardware.kt#L34-L47)

Don't assume that the car's data is available at all times. If you get an error, check the [status](https://developer.android.com/reference/androidx/car/app/hardware/common/CarValue#getStatus\(\)) of the value you requested to better understand why the data you requested couldn't be retrieved. To learn more about the `CarInfo` class definition, see the [reference documentation](https://developer.android.com/reference/androidx/car/app/hardware/info/CarInfo).

## CarSensors

The [`CarSensors`](https://developer.android.com/reference/androidx/car/app/hardware/info/CarSensors) class gives you access to the vehicle's accelerometer, gyroscope, compass, and location data. The availability of these values might depend on the OEM. The format for the data from the accelerometer, gyroscope, and compass is the same as you would get from the [`SensorManager` API](https://developer.android.com/reference/android/hardware/SensorManager).

For example, to check the vehicle's heading:
    
    
    val carSensors = carContext.getCarService(CarHardwareManager::class.java).carSensors
    
    val listener = OnCarDataAvailableListener<Compass> { data ->
        if (data.orientations.status == CarValue.STATUS_SUCCESS) {
            val orientation = data.orientations.value
        } else {
            // Data not available, handle error
        }
    }
    
    carSensors.addCompassListener(CarSensors.UPDATE_RATE_NORMAL, carContext.mainExecutor, listener)
    // ...
    // Unregister the listener when you no longer need updates
    carSensors.removeCompassListener(listener)
    
    [CarHardware.kt](https://github.com/android/snippets/blob/fb394b64d62824710fc9bc52b62fd4e1c276b431/cars/src/main/java/com/example/cars/apps/library/CarHardware.kt#L54-L67)

To access location data from the car, you must also declare and request the `android.permission.ACCESS_FINE_LOCATION` permission.

**Caution:** On Android Automotive OS, `CarSensors` data returns [`STATUS_UNIMPLEMENTED`](https://developer.android.com/reference/androidx/car/app/hardware/common/CarValue#STATUS_UNIMPLEMENTED\(\)). Instead, use standard Android APIs to access the data, such as `SensorManager` or [`LocationManager`](https://developer.android.com/reference/android/location/LocationManager).

## Test

To simulate sensor data when testing on Android Auto, see the [Sensors](https://developer.android.com/training/cars/testing/dhu#sensors) and [Sensor configuration](https://developer.android.com/training/cars/testing/dhu#sensor-configuration) sections of the Desktop Head Unit guide. To simulate sensor data when testing on Android Automotive OS, see [Emulate hardware state](https://developer.android.com/training/cars/testing/emulator#emulate-state) in the Android Automotive OS emulator guide.

[ Previous arrow_back  Constraints API  ](https://developer.android.com/training/cars/apps/library/constraints-api)

[ Next Record from the car microphone  arrow_forward  ](https://developer.android.com/training/cars/apps/library/car-microphone)

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-09-08 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-08 UTC."],[],[]] 
