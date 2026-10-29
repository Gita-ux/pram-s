document.addEventListener("DOMContentLoaded", () => {
  /* ---------- Header : effet au scroll ---------- */
  const header = document.querySelector(".header");
  const onScroll = () => {
    if (window.scrollY > 30) {
      header?.classList.add("is-scrolled");
    } else {
      header?.classList.remove("is-scrolled");
    }
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Menu mobile ---------- */
  const burger = document.querySelector(".burger");
  const nav = document.querySelector(".nav");
  burger?.addEventListener("click", () => {
    burger.classList.toggle("is-active");
    nav?.classList.toggle("is-open");
  });
  document.querySelectorAll(".nav__link").forEach((link) => {
    link.addEventListener("click", () => {
      burger?.classList.remove("is-active");
      nav?.classList.remove("is-open");
    });
  });

  /* ---------- Animation au défilement (reveal) ---------- */
  const revealEls = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && revealEls.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    revealEls.forEach((el) => observer.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  }

  /* ---------- Compteurs animés ---------- */
  const counters = document.querySelectorAll("[data-counter]");
  const animateCounter = (el) => {
    const target = parseInt(el.dataset.counter, 10) || 0;
    const duration = 1400;
    const start = performance.now();
    const step = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      el.textContent = Math.floor(progress * target).toLocaleString("fr-FR");
      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        el.textContent = target.toLocaleString("fr-FR");
      }
    };
    requestAnimationFrame(step);
  };
  if ("IntersectionObserver" in window && counters.length) {
    const counterObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );
    counters.forEach((el) => counterObserver.observe(el));
  }

  /* ---------- Filtres de la galerie de réalisations (sans rechargement) ---------- */
  const filterButtons = document.querySelectorAll("[data-filter]");
  const galleryItems = document.querySelectorAll("[data-category]");
  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterButtons.forEach((b) => b.classList.remove("is-active"));
      btn.classList.add("is-active");
      const filter = btn.dataset.filter;
      galleryItems.forEach((item) => {
        const show = filter === "all" || item.dataset.category === filter;
        item.style.display = show ? "" : "none";
      });
    });
  });

  /* ---------- Aperçu du nom des fichiers sélectionnés (formulaire devis) ---------- */
  const fileInput = document.querySelector('input[type="file"][multiple]');
  const filePreview = document.querySelector("#file-preview");
  fileInput?.addEventListener("change", () => {
    if (!filePreview) return;
    const files = Array.from(fileInput.files || []);
    filePreview.innerHTML = files
      .map((f) => `<span class="file-chip"><i class="bi bi-paperclip"></i> ${f.name}</span>`)
      .join("");
  });

  /* ---------- Fermer les messages flash automatiquement ---------- */
  document.querySelectorAll(".alert").forEach((alert) => {
    setTimeout(() => {
      alert.style.transition = "opacity 0.5s ease";
      alert.style.opacity = "0";
      setTimeout(() => alert.remove(), 500);
    }, 6000);
  });
});
