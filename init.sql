DO $$
BEGIN
    -- Create the devices table if it does not exist
    IF NOT EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'devices') THEN
        CREATE TABLE devices (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL
        );
    END IF;

    -- Create the sensor_data table if it does not exist
    IF NOT EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'sensor_data') THEN
        CREATE TABLE sensor_data (
            id UUID PRIMARY KEY,
            device_id VARCHAR(255) NOT NULL,
            type VARCHAR(255) NOT NULL,
            value JSONB NOT NULL,
            timestamp TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (device_id) REFERENCES devices(id)
        );
    END IF;
END $$;