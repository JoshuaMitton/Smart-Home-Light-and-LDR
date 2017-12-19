CREATE FUNCTION addDevice (p_name VARCHAR(45), p_type VARCHAR(45), p_ip VARCHAR(15))
BEGIN
  INSERT INTO devices (device_name, device_type, device_ip) VALUES (p_name, p_type, p_ip);
END
