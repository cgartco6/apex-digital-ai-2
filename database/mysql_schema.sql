CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255),
  role VARCHAR(50),
  password_hash VARCHAR(255)
);

CREATE TABLE payments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  gateway VARCHAR(50),
  amount DECIMAL(10,2),
  status VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    agency_id INT,
    action VARCHAR(255),
    details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_id INT,
    action VARCHAR(255)
);

ALTER TABLE clients ADD COLUMN role_id INT DEFAULT 3; -- 3 = client

CREATE TABLE marketplace_services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    agency_id INT,
    name VARCHAR(255),
    category VARCHAR(100),
    description TEXT,
    price DECIMAL(10,2),
    currency VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE marketplace_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT,
    buyer_id INT,
    amount DECIMAL(10,2),
    currency VARCHAR(10),
    platform_fee DECIMAL(10,2),
    agency_share DECIMAL(10,2),
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE marketplace_reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT,
    user_id INT,
    rating INT,
    review TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
